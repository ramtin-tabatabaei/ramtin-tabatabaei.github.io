(function () {
  var carousel = document.querySelector("[data-home-research-carousel]");

  if (!carousel) {
    return;
  }

  var slides = Array.prototype.slice.call(
    carousel.querySelectorAll("[data-home-research-slide]")
  );
  var currentSlide = carousel.querySelector("[data-current-slide]");
  var totalSlides = carousel.querySelector("[data-total-slides]");
  var currentIndex = 0;

  function syncVideos() {
    slides.forEach(function (slide, index) {
      var iframe = slide.querySelector("iframe[data-video-src]");

      if (!iframe) {
        return;
      }

      var videoSrc = iframe.getAttribute("data-video-src");
      if (!videoSrc) {
        return;
      }

      if (index === currentIndex) {
        if (iframe.getAttribute("src") !== videoSrc) {
          iframe.setAttribute("src", videoSrc);
        }
      } else if (iframe.getAttribute("src")) {
        iframe.removeAttribute("src");
      }
    });
  }

  function renderSlide() {
    slides.forEach(function (slide, index) {
      var isActive = index === currentIndex;
      slide.classList.toggle("is-active", isActive);
      slide.hidden = !isActive;
    });

    if (currentSlide) {
      currentSlide.textContent = String(currentIndex + 1);
    }

    syncVideos();
  }

  if (totalSlides) {
    totalSlides.textContent = String(slides.length);
  }

  carousel
    .querySelectorAll("[data-slide-direction]")
    .forEach(function (button) {
      button.addEventListener("click", function () {
        var direction =
          parseInt(button.getAttribute("data-slide-direction"), 10) || 0;

        currentIndex = (currentIndex + direction + slides.length) % slides.length;
        renderSlide();
      });
    });

  renderSlide();
})();
