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

  function renderSlide() {
    slides.forEach(function (slide, index) {
      var isActive = index === currentIndex;
      slide.classList.toggle("is-active", isActive);
      slide.hidden = !isActive;
    });

    if (currentSlide) {
      currentSlide.textContent = String(currentIndex + 1);
    }
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
