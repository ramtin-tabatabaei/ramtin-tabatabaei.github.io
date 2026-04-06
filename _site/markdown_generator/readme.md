# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.

## Paper showcase generator

`generate_paper_showcase.py` is a local CLI that creates a polished `_publications/*.md` page using the custom `paper-showcase` layout.

It expects:

- a paper directory containing a PDF and any local assets
- optionally, an Overleaf source directory with `.tex` / `.bib` files
- `OPENAI_API_KEY` set in your shell

Example:

```bash
export OPENAI_API_KEY=...
python3 markdown_generator/generate_paper_showcase.py \
  /absolute/path/to/paper_assets \
  --overleaf-dir /absolute/path/to/overleaf_project \
  --featured
```

To create a new page with an explicit website path:

```bash
python3 markdown_generator/generate_paper_showcase.py \
  /absolute/path/to/paper.pdf \
  --slug chi2026-robotfailure \
  --permalink /publication/CHI2026-RobotFailure/ \
  --featured
```

To update an existing publication page instead of creating a new `_publications/*.md`
file, point the script at the existing page by permalink, slug, or markdown path:

```bash
python3 markdown_generator/generate_paper_showcase.py \
  /absolute/path/to/paper.pdf \
  --existing-page /publication/gazing-at-failure/ \
  --overwrite
```

When `--existing-page` is used, the script keeps that page's permalink and reuses its
current `featured` / `category` values unless you explicitly override them.

The script will:

1. upload the paper PDF to OpenAI
2. read local LaTeX/BibTeX context
3. generate structured page content
4. copy the paper PDF, selected images, and an optional local demo video into this site
5. write a paper page into `_publications/`

If you want to preview the generated Markdown without writing files, use `--dry-run`.
