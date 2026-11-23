/* Small progressive enhancements: silent preview loops on project cards and a gentle scroll reveal. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  // Project card previews: load and play only while on screen; keep the poster for reduced motion.
  var previews = document.querySelectorAll('video.project-card__preview[data-src]');
  if (!reduce && hasIO && previews.length) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          if (!v.src) { v.src = v.getAttribute('data-src'); }
          var p = v.play(); if (p && p.catch) { p.catch(function () {}); }
        } else if (v.src) { v.pause(); }
      });
    }, { threshold: 0.35 });
    previews.forEach(function (v) { vio.observe(v); });
  }

  // Scroll reveal: only added when JS runs, so content is always visible without it.
  if (!reduce && hasIO) {
    var items = document.querySelectorAll('.academic-section, .project-card, .system-card, .publication-entry, .research-directions > div');
    document.documentElement.classList.add('reveal-ready');
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); rio.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { rio.observe(el); });
  }
})();
