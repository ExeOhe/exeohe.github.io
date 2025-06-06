const container = document.querySelector('.scrollable-container');
let scrollAmount = 0;
const scrollStep = 1;
const scrollDelay = 100;
const fadeDuration = 500; // ms, should match your CSS transition

function autoScroll() {
  if (container) {
    scrollAmount += scrollStep;
    if (scrollAmount > container.scrollWidth - container.clientWidth) {
      // Fade out
      container.classList.add('scroll-fade');
      setTimeout(() => {
        // Jump back to start while faded out
        scrollAmount = 0;
        container.scrollLeft = scrollAmount;
        // Fade in
        container.classList.remove('scroll-fade');
        setTimeout(autoScroll, scrollDelay);
      }, fadeDuration);
      return;
    }
    container.scrollLeft = scrollAmount;
    setTimeout(autoScroll, scrollDelay);
  }
}
autoScroll();