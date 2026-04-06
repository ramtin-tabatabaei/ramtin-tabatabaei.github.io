#!/usr/bin/env python3
"""Generate a publication showcase page from a local paper directory.

The script:
1. reads a paper directory and optional Overleaf source directory
2. uploads the paper PDF to OpenAI for multimodal extraction
3. asks the model for structured page content
4. copies paper assets into the site
5. writes a Jekyll publication page using the paper-showcase layout
"""

from __future__ import annotations

import argparse
from html import escape
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - handled at runtime
    OpenAI = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_DIR = PROJECT_ROOT / "_publications"
IMAGE_ROOT = PROJECT_ROOT / "images" / "papers"
FILE_ROOT = PROJECT_ROOT / "files" / "papers"

TEXT_EXTENSIONS = {".tex", ".bib", ".txt", ".md"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
VIDEO_EXTENSIONS = {".mp4", ".webm", ".ogg", ".mov"}
IGNORED_SOURCE_SUFFIXES = {
    ".aux",
    ".bbl",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".run.xml",
    ".synctex.gz",
    ".toc",
}


SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "title": {"type": "string"},
        "subtitle": {"type": "string"},
        "venue": {"type": "string"},
        "publication_date": {"type": "string"},
        "excerpt": {"type": "string"},
        "abstract": {"type": "string"},
        "overview": {"type": "string"},
        "method": {"type": "string"},
        "findings": {"type": "string"},
        "limitations": {"type": "string"},
        "future_work": {"type": "string"},
        "citation": {"type": "string"},
        "citation_bibtex": {"type": "string"},
        "awards": {"type": "array", "items": {"type": "string"}},
        "key_contributions": {"type": "array", "items": {"type": "string"}},
        "authors": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string"},
                    "affiliation": {"type": "string"},
                    "url": {"type": "string"},
                },
                "required": ["name", "affiliation", "url"],
            },
        },
        "external_links": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "label": {"type": "string"},
                    "url": {"type": "string"},
                },
                "required": ["label", "url"],
            },
        },
    },
    "required": [
        "title",
        "subtitle",
        "venue",
        "publication_date",
        "excerpt",
        "abstract",
        "overview",
        "method",
        "findings",
        "limitations",
        "future_work",
        "citation",
        "citation_bibtex",
        "awards",
        "key_contributions",
        "authors",
        "external_links",
    ],
}


SYSTEM_PROMPT = dedent(
    """
    You create structured content for academic project websites.

    Your task is to read the provided paper PDF and optional Overleaf source
    excerpts, then prepare content for a project page similar to a research
    showcase website.

    Rules:
    - Use only information grounded in the provided materials.
    - Do not invent awards, author links, demo URLs, affiliations, figures, or
      publication dates.
    - If a field is unknown, return an empty string or an empty list.
    - Write concise, polished website copy.
    - Keep the abstract faithful to the paper rather than rewriting it into
      marketing language.
    - For `publication_date`, use YYYY-MM-DD when the date is explicit.
    - For `external_links`, only include links that appear in the provided
      material or are obvious canonical paper links such as arXiv or DOI links.
    - For `key_contributions`, return 3 to 5 short bullet-ready points when
      enough evidence exists.
    """
).strip()


@dataclass
class AssetBundle:
    pdf: Path | None
    teaser_image: Path | None
    gallery_images: list[Path]
    demo_video: Path | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Jekyll paper showcase page from local paper assets."
    )
    parser.add_argument(
        "paper_dir",
        type=Path,
        help="Directory containing the paper assets, or a direct path to the paper PDF.",
    )
    parser.add_argument(
        "--overleaf-dir",
        type=Path,
        default=None,
        help="Optional Overleaf source directory. Defaults to paper_dir.",
    )
    parser.add_argument(
        "--existing-page",
        default=None,
        help=(
            "Existing publication page to update. Accepts a markdown path, a "
            "permalink like /publication/gazing-at-failure/, or a slug."
        ),
    )
    parser.add_argument("--slug", default=None, help="URL slug for the generated page.")
    parser.add_argument(
        "--permalink",
        default=None,
        help="Custom permalink for a new generated page, such as /publication/CHI2026-RobotFailure/.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o",
        help="OpenAI model for extraction. Defaults to gpt-4o.",
    )
    parser.add_argument(
        "--category",
        default=None,
        help="Publication category front matter. Defaults to the existing page category or conferences.",
    )
    parser.add_argument(
        "--featured",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Whether the generated page should be featured. Defaults to the existing page value or false.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the target markdown file if it already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated markdown instead of writing files.",
    )
    parser.add_argument(
        "--max-source-chars",
        type=int,
        default=50000,
        help="Maximum number of source-text characters to send from Overleaf files.",
    )
    parser.add_argument(
        "--max-gallery-images",
        type=int,
        default=4,
        help="Maximum number of local images to copy into the figure gallery.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return cleaned or "paper-showcase"


def choose_best_pdf(paths: list[Path]) -> Path | None:
    if not paths:
        return None
    ranked = sorted(
        paths,
        key=lambda path: (
            0 if "camera" in path.stem.lower() else 1,
            0 if "paper" in path.stem.lower() else 1,
            -path.stat().st_size,
        ),
    )
    return ranked[0]


def resolve_paper_input(path: Path) -> tuple[Path, Path | None]:
    resolved = path.resolve()
    if resolved.is_file():
        if resolved.suffix.lower() != ".pdf":
            raise RuntimeError(
                f"Expected a directory or PDF file, but got: {resolved}"
            )
        return resolved.parent, resolved
    return resolved, None


def unquote_yaml_scalar(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in {"'", '"'}:
        return stripped[1:-1]
    return stripped


def parse_yaml_bool(value: str) -> bool | None:
    normalized = value.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    return None


def read_front_matter_value(path: Path, key: str) -> str:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""

    if not content.startswith("---"):
        return ""

    front_matter, _, _ = content[3:].partition("\n---")
    if not front_matter:
        return ""

    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", front_matter)
    if not match:
        return ""
    return unquote_yaml_scalar(match.group(1))


def normalize_publication_locator(value: str) -> str:
    candidate = value.strip()
    if not candidate:
        raise RuntimeError("Existing publication target cannot be empty.")
    if candidate.startswith("/"):
        return "/" + candidate.strip("/") + "/"
    if "/" in candidate:
        return "/" + candidate.strip("/") + "/"
    return f"/publication/{slugify(candidate)}/"


def permalink_slug(permalink: str) -> str:
    stem = permalink.strip("/").split("/")[-1]
    return slugify(stem)


def normalize_permalink(value: str) -> str:
    candidate = value.strip()
    if not candidate:
        raise RuntimeError("Permalink cannot be empty.")
    return "/" + candidate.strip("/") + "/"


def resolve_existing_publication(value: str) -> tuple[Path, str, str]:
    candidate_path = Path(value).expanduser()
    if not candidate_path.is_absolute():
        candidate_path = PROJECT_ROOT / candidate_path

    if candidate_path.exists():
        permalink = read_front_matter_value(candidate_path, "permalink")
        if not permalink:
            raise RuntimeError(
                f"Existing page is missing a permalink in front matter: {candidate_path}"
            )
        return candidate_path, permalink, permalink_slug(permalink)

    target_permalink = normalize_publication_locator(value)
    for path in sorted(PUBLICATIONS_DIR.glob("*.md")):
        permalink = read_front_matter_value(path, "permalink")
        if permalink == target_permalink:
            return path, permalink, permalink_slug(permalink)

    raise FileNotFoundError(
        f"No publication file matched {value!r}. Looked for permalink {target_permalink}."
    )


def rank_image(path: Path) -> tuple[int, int, str]:
    stem = path.stem.lower()
    score = 10
    keywords = [
        ("teaser", 0),
        ("overview", 1),
        ("hero", 2),
        ("pipeline", 3),
        ("architecture", 4),
        ("system", 5),
        ("fig1", 6),
        ("figure1", 6),
    ]
    for keyword, keyword_score in keywords:
        if keyword in stem:
            score = keyword_score
            break
    return (score, len(path.name), path.name.lower())


def discover_assets(root: Path, max_gallery_images: int, preferred_pdf: Path | None = None) -> AssetBundle:
    pdfs: list[Path] = []
    images: list[Path] = []
    videos: list[Path] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            pdfs.append(path)
        elif suffix in IMAGE_EXTENSIONS:
            images.append(path)
        elif suffix in VIDEO_EXTENSIONS:
            videos.append(path)

    pdf = preferred_pdf if preferred_pdf is not None else choose_best_pdf(pdfs)
    sorted_images = sorted(images, key=rank_image)
    teaser = sorted_images[0] if sorted_images else None
    gallery_images = sorted_images[:max_gallery_images]
    demo_video = videos[0] if videos else None
    return AssetBundle(pdf=pdf, teaser_image=teaser, gallery_images=gallery_images, demo_video=demo_video)


def load_source_context(source_root: Path, max_chars: int) -> str:
    candidates: list[Path] = []
    for path in source_root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in IGNORED_SOURCE_SUFFIXES:
            continue
        if suffix in TEXT_EXTENSIONS:
            candidates.append(path)

    candidates.sort(
        key=lambda path: (
            0 if path.name.lower() == "main.tex" else 1,
            0 if path.suffix.lower() == ".tex" else 1,
            len(path.parts),
            path.name.lower(),
        )
    )

    chunks: list[str] = []
    consumed = 0

    for path in candidates:
        try:
            content = path.read_text(encoding="utf-8", errors="ignore").strip()
        except OSError:
            continue

        if not content:
            continue

        snippet = f"\n\n=== FILE: {path.relative_to(source_root)} ===\n{content}"
        remaining = max_chars - consumed
        if remaining <= 0:
            break
        if len(snippet) > remaining:
            snippet = snippet[:remaining]
        chunks.append(snippet)
        consumed += len(snippet)

    return "".join(chunks).strip()


def build_asset_manifest(bundle: AssetBundle, root: Path) -> str:
    items: list[str] = []
    if bundle.pdf:
        items.append(f"PDF: {bundle.pdf.relative_to(root)}")
    if bundle.teaser_image:
        items.append(f"Suggested teaser image: {bundle.teaser_image.relative_to(root)}")
    if bundle.gallery_images:
        items.append(
            "Candidate images: "
            + ", ".join(str(path.relative_to(root)) for path in bundle.gallery_images)
        )
    if bundle.demo_video:
        items.append(f"Demo video: {bundle.demo_video.relative_to(root)}")
    return "\n".join(items)


def require_openai_client() -> Any:
    if OpenAI is None:
        raise RuntimeError(
            "The `openai` package is not installed. Install it with `pip install openai`."
        )
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Export it in your shell before running this script."
        )
    return OpenAI()


def extract_page_data(
    client: Any,
    model: str,
    pdf: Path | None,
    source_context: str,
    asset_manifest: str,
    project_hint: str,
) -> dict[str, Any]:
    user_content: list[dict[str, str]] = []

    if pdf:
        with pdf.open("rb") as pdf_file:
            uploaded = client.files.create(file=pdf_file, purpose="user_data")
        user_content.append({"type": "input_file", "file_id": uploaded.id})

    prompt_parts = [
        f"Project hint: {project_hint}",
        "Prepare structured content for a paper showcase page.",
    ]

    if source_context:
        prompt_parts.append("Overleaf/source excerpts:\n" + source_context)
    if asset_manifest:
        prompt_parts.append("Local asset manifest:\n" + asset_manifest)

    user_content.append({"type": "input_text", "text": "\n\n".join(prompt_parts)})

    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
            {"role": "user", "content": user_content},
        ],
        max_output_tokens=3000,
        text={
            "format": {
                "type": "json_schema",
                "name": "paper_showcase_page",
                "strict": True,
                "schema": SCHEMA,
            }
        },
    )

    payload = response.output_text.strip()
    if not payload:
        raise RuntimeError("OpenAI returned an empty response.")
    return json.loads(payload)


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def copy_if_present(source: Path | None, destination: Path | None) -> None:
    if source is None or destination is None:
        return
    ensure_directory(destination.parent)
    shutil.copy2(source, destination)


def humanize_stem(path: Path) -> str:
    text = path.stem.replace("_", " ").replace("-", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:1].upper() + text[1:] if text else path.name


def to_yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return '""'
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def dump_yaml_lines(value: Any, indent: int = 0) -> list[str]:
    prefix = " " * indent
    if isinstance(value, dict):
        lines: list[str] = []
        for key, item in value.items():
            if item in ("", [], {}, None):
                continue
            if isinstance(item, (dict, list)):
                lines.append(f"{prefix}{key}:")
                lines.extend(dump_yaml_lines(item, indent + 2))
            else:
                lines.append(f"{prefix}{key}: {to_yaml_scalar(item)}")
        return lines

    if isinstance(value, list):
        lines = []
        for item in value:
            if isinstance(item, dict):
                lines.append(f"{prefix}-")
                lines.extend(dump_yaml_lines(item, indent + 2))
            elif isinstance(item, list):
                lines.append(f"{prefix}-")
                lines.extend(dump_yaml_lines(item, indent + 2))
            else:
                lines.append(f"{prefix}- {to_yaml_scalar(item)}")
        return lines

    return [f"{prefix}{to_yaml_scalar(value)}"]


def build_front_matter(data: dict[str, Any]) -> str:
    ordered: dict[str, Any] = {
        "layout": "paper-showcase",
        "title": data.get("title", ""),
        "collection": "publications",
        "category": data.get("category", "conferences"),
        "permalink": data.get("permalink", ""),
        "featured": data.get("featured", False),
        "excerpt": data.get("excerpt", ""),
        "venue": data.get("venue", ""),
        "date": data.get("date", ""),
        "subtitle": data.get("subtitle", ""),
        "teaser_image": data.get("teaser_image", ""),
        "teaser_alt": data.get("teaser_alt", ""),
        "teaser_caption": data.get("teaser_caption", ""),
        "demo_video": data.get("demo_video", ""),
        "abstract": data.get("abstract", ""),
        "citation": data.get("citation", ""),
        "citation_bibtex": data.get("citation_bibtex", ""),
        "authors": data.get("authors", []),
        "awards": data.get("awards", []),
        "hero_links": data.get("hero_links", []),
        "paperurl": data.get("paperurl", ""),
    }
    lines = ["---"]
    lines.extend(dump_yaml_lines(ordered))
    lines.append("---")
    return "\n".join(lines)


def build_gallery_section(slug: str, gallery_images: list[Path], teaser_name: str | None) -> str:
    figure_blocks: list[str] = []
    for image_path in gallery_images:
        if teaser_name and image_path.name == teaser_name:
            continue
        rel = f"/images/papers/{slug}/{image_path.name}"
        label = escape(humanize_stem(image_path))
        figure_blocks.append(
            "\n".join(
                [
                    '  <figure class="paper-showcase__figure-card">',
                    f'    <img src="{rel}" alt="{label}">',
                    f"    <figcaption>{label}</figcaption>",
                    "  </figure>",
                ]
            )
        )
    if not figure_blocks:
        return ""
    joined = "\n".join(figure_blocks)
    return "\n".join(
        [
            '<section class="paper-showcase__panel paper-showcase__panel--gallery">',
            "  <h2>Figure Highlights</h2>",
            '  <div class="paper-showcase__figure-row">',
            joined,
            "  </div>",
            "</section>",
            "",
        ]
    )


def text_to_paragraphs_html(text: str, fallback: str) -> str:
    content = text.strip() or fallback
    paragraphs = [segment.strip() for segment in re.split(r"\n\s*\n", content) if segment.strip()]
    if not paragraphs:
        paragraphs = [fallback]
    return "\n".join(f"<p>{escape(paragraph)}</p>" for paragraph in paragraphs)


def items_to_list_html(items: list[str], fallback: list[str]) -> str:
    values = items or fallback
    list_items = "\n".join(f"    <li>{escape(item)}</li>" for item in values)
    return "\n".join(["  <ul>", list_items, "  </ul>"])


def build_content_section(title: str, body_html: str, modifier: str = "") -> str:
    classes = "paper-showcase__panel"
    if modifier:
        classes += f" {modifier}"
    return "\n".join(
        [
            f'<section class="{classes}">',
            f"  <h2>{escape(title)}</h2>",
            body_html,
            "</section>",
            "",
        ]
    )


def build_markdown_body(page: dict[str, Any], slug: str, gallery_images: list[Path], teaser_name: str | None) -> str:
    sections: list[str] = []

    overview = page.get("overview") or ""
    sections.append(
        build_content_section(
            "Overview",
            text_to_paragraphs_html(overview, "Add an overview of the paper here."),
            "paper-showcase__panel--overview",
        )
    )

    contributions = page.get("key_contributions") or []
    sections.append(
        build_content_section(
            "Key Contributions",
            items_to_list_html(
                contributions,
                ["Add contribution 1.", "Add contribution 2.", "Add contribution 3."],
            ),
            "paper-showcase__panel--contributions",
        )
    )

    method = page.get("method") or ""
    sections.append(
        build_content_section(
            "Method and System",
            text_to_paragraphs_html(
                method,
                "Add a short explanation of the system, method, or study design here.",
            ),
            "paper-showcase__panel--method",
        )
    )

    findings = page.get("findings") or ""
    sections.append(
        build_content_section(
            "Results Overview",
            text_to_paragraphs_html(
                findings,
                "Add the main findings, evaluation results, or takeaways here.",
            ),
            "paper-showcase__panel--results",
        )
    )

    sections.append(
        build_content_section(
            "Quantitative Results",
            text_to_paragraphs_html(
                "",
                "Add quantitative results here, such as participant counts, statistical tests, effect sizes, or comparisons between conditions.",
            ),
            "paper-showcase__panel--results-alt",
        )
    )

    sections.append(
        build_content_section(
            "Qualitative Insights",
            text_to_paragraphs_html(
                "",
                "Add qualitative observations here, such as participant feedback, notable behaviors, or themes that explain the quantitative results.",
            ),
            "paper-showcase__panel--results-soft",
        )
    )

    limitations = page.get("limitations", "").strip()
    future_work = page.get("future_work", "").strip()
    if limitations or future_work:
        body: list[str] = []
        if limitations:
            body.append("<h3>Limitations</h3>")
            body.append(text_to_paragraphs_html(limitations, ""))
        if future_work:
            body.append("<h3>Future Work</h3>")
            body.append(text_to_paragraphs_html(future_work, ""))
        sections.append(
            build_content_section(
                "Discussion",
                "\n".join(body),
                "paper-showcase__panel--discussion",
            )
        )
    else:
        sections.append(
            build_content_section(
                "Discussion",
                text_to_paragraphs_html(
                    "",
                    "Add design implications, limitations, and future directions here.",
                ),
                "paper-showcase__panel--discussion",
            )
        )

    gallery = build_gallery_section(slug, gallery_images, teaser_name)
    if gallery:
        sections.append(gallery)

    return "\n".join(sections).strip() + "\n"


def unique_links(links: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    output: list[dict[str, str]] = []
    for link in links:
        label = (link.get("label") or "").strip()
        url = (link.get("url") or "").strip()
        if not label or not url:
            continue
        key = (label, url)
        if key in seen:
            continue
        seen.add(key)
        output.append({"label": label, "url": url})
    return output


def choose_paper_url(links: list[dict[str, str]]) -> str:
    priorities = ("paper", "pdf", "doi", "arxiv")
    for priority in priorities:
        for link in links:
            if priority in link["label"].lower():
                return link["url"]
    return links[0]["url"] if links else ""


def normalize_page_data(
    extracted: dict[str, Any],
    slug: str,
    permalink: str,
    category: str,
    featured: bool,
    local_pdf_url: str,
    local_video_url: str,
    teaser_image_url: str,
) -> dict[str, Any]:
    external_links = unique_links(extracted.get("external_links", []))
    hero_links = []
    if local_pdf_url:
        hero_links.append({"label": "Paper PDF", "url": local_pdf_url})
    if local_video_url:
        hero_links.append({"label": "Demo Video", "url": local_video_url})
    hero_links.extend(external_links)
    hero_links = unique_links(hero_links)

    title = extracted.get("title", "").strip() or slug.replace("-", " ").title()
    excerpt = extracted.get("excerpt", "").strip()
    abstract = extracted.get("abstract", "").strip()
    if not excerpt:
        excerpt = (abstract or extracted.get("overview", "")).strip()
        excerpt = excerpt[:180].rsplit(" ", 1)[0] if len(excerpt) > 180 else excerpt

    publication_date = extracted.get("publication_date", "").strip()
    if publication_date and not re.match(r"^\d{4}-\d{2}-\d{2}$", publication_date):
        publication_date = ""

    return {
        "title": title,
        "collection": "publications",
        "category": category,
        "permalink": permalink,
        "featured": featured,
        "excerpt": excerpt,
        "venue": extracted.get("venue", "").strip(),
        "date": publication_date,
        "subtitle": extracted.get("subtitle", "").strip(),
        "teaser_image": teaser_image_url,
        "teaser_alt": title,
        "teaser_caption": "",
        "demo_video": local_video_url,
        "abstract": abstract,
        "citation": extracted.get("citation", "").strip(),
        "citation_bibtex": extracted.get("citation_bibtex", "").strip(),
        "authors": extracted.get("authors", []),
        "awards": extracted.get("awards", []),
        "hero_links": hero_links,
        "paperurl": choose_paper_url(hero_links),
        "overview": extracted.get("overview", "").strip(),
        "key_contributions": extracted.get("key_contributions", []),
        "method": extracted.get("method", "").strip(),
        "findings": extracted.get("findings", "").strip(),
        "limitations": extracted.get("limitations", "").strip(),
        "future_work": extracted.get("future_work", "").strip(),
    }


def write_output(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Re-run with --overwrite to replace it.")
    ensure_directory(path.parent)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    paper_dir, explicit_pdf = resolve_paper_input(args.paper_dir)
    overleaf_dir = (args.overleaf_dir or paper_dir).resolve()

    if not paper_dir.exists():
        raise FileNotFoundError(f"Paper directory does not exist: {paper_dir}")
    if not overleaf_dir.exists():
        raise FileNotFoundError(f"Overleaf directory does not exist: {overleaf_dir}")

    assets = discover_assets(
        paper_dir,
        args.max_gallery_images,
        preferred_pdf=explicit_pdf,
    )
    source_context = load_source_context(overleaf_dir, args.max_source_chars)

    if not assets.pdf and not source_context:
        raise RuntimeError("No paper PDF or readable source files were found.")

    client = require_openai_client()

    project_hint = f"Source directory name: {paper_dir.name}"
    asset_manifest = build_asset_manifest(assets, paper_dir)
    extracted = extract_page_data(
        client=client,
        model=args.model,
        pdf=assets.pdf,
        source_context=source_context,
        asset_manifest=asset_manifest,
        project_hint=project_hint,
    )

    existing_category = ""
    existing_featured: bool | None = None

    if args.existing_page:
        output_path, permalink, slug = resolve_existing_publication(args.existing_page)
        existing_category = read_front_matter_value(output_path, "category")
        existing_featured = parse_yaml_bool(read_front_matter_value(output_path, "featured"))
    else:
        raw_slug = args.slug or extracted.get("title") or paper_dir.name
        slug = slugify(raw_slug)
        permalink = normalize_permalink(args.permalink) if args.permalink else f"/publication/{slug}/"
        output_path = PUBLICATIONS_DIR / f"{slug}.md"

    teaser_image_url = (
        f"/images/papers/{slug}/{assets.teaser_image.name}" if assets.teaser_image else ""
    )
    local_pdf_url = (
        f"/files/papers/{slug}/{assets.pdf.name}" if assets.pdf else ""
    )
    local_video_url = (
        f"/files/papers/{slug}/{assets.demo_video.name}" if assets.demo_video else ""
    )

    page = normalize_page_data(
        extracted=extracted,
        slug=slug,
        permalink=permalink,
        category=args.category or existing_category or "conferences",
        featured=args.featured if args.featured is not None else (existing_featured or False),
        local_pdf_url=local_pdf_url,
        local_video_url=local_video_url,
        teaser_image_url=teaser_image_url,
    )

    front_matter = build_front_matter(page)
    body = build_markdown_body(
        page=page,
        slug=slug,
        gallery_images=assets.gallery_images,
        teaser_name=assets.teaser_image.name if assets.teaser_image else None,
    )

    content = front_matter + "\n\n" + body

    if args.dry_run:
        print(content)
        return 0

    if assets.pdf:
        target_pdf = FILE_ROOT / slug / assets.pdf.name
        copy_if_present(assets.pdf, target_pdf)

    if assets.demo_video:
        target_video = FILE_ROOT / slug / assets.demo_video.name
        copy_if_present(assets.demo_video, target_video)

    for image in assets.gallery_images:
        target_image = IMAGE_ROOT / slug / image.name
        copy_if_present(image, target_image)

    write_output(output_path, content, overwrite=args.overwrite)
    print(f"Wrote {output_path.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - CLI surface
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
