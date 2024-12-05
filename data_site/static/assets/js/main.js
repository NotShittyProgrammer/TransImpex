(function() {

  "use strict";
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

   const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        aos_init();
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfokio-lightbox'
  });


  /**
   * Animation on scroll
   */
  function aos_init() {
    AOS.init({
      duration: 900,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', () => {
    aos_init();
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

})();
//
let navButtons = document.querySelectorAll('.nav-link');
navButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          let link = this.getAttribute('href');
          if (window.location.pathname === link) {
              event.preventDefault();
          }
      });
  });
// window.onload = function () {
//   document.querySelector(".preloader").style.display = "none";
// }


document.querySelector('.back-to-top').addEventListener('click', function(event) {
    event.preventDefault();
    document.querySelector('header').scrollIntoView({ behavior: 'smooth' });
});