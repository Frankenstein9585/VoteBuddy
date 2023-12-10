  document.addEventListener('DOMContentLoaded', function () {
    var accordion = new bootstrap.Collapse(document.getElementById('accordionExample'), {
      toggle: false
    });

    accordion._element.addEventListener('show.bs.collapse', function (event) {
      // Close the previously open accordion item
      var previouslyOpenItem = accordion._element.querySelector('.accordion-item:not(.collapsed)');
      if (previouslyOpenItem && previouslyOpenItem !== event.target.parentElement) {
        accordion.hide(previouslyOpenItem.querySelector('.accordion-collapse'));
      }

      // Scroll to the top of the opened accordion item's button
      var openedItemButton = event.target.closest('.accordion-item').querySelector('.accordion-button');
      if (openedItemButton) {
        setTimeout(function() {
          openedItemButton.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
            inline: 'start' // This ensures the left edge of the element is aligned with the left edge of the visible area of the scrollable ancestor
          });
        }, 300); // Adjust the delay as needed
      }
    });
  });