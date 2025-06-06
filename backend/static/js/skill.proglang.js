const container = document.querySelector('.scrollable-container');
let scrollAmount = 0;
const scrollStep = 1;
const scrollDelay = 20;

function autoScroll() {
  if (container) {
    scrollAmount += scrollStep;
    if (scrollAmount > container.scrollWidth - container.clientWidth) {
      scrollAmount = 0;
    }
    container.scrollLeft = scrollAmount;
    setTimeout(autoScroll, scrollDelay);
  }
}
autoScroll();