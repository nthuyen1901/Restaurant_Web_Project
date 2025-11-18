// Initialisation d’Isotope
$(window).on('load', function () {

  // Initialisation isotope
  var $grid = $(".grid").isotope({
    itemSelector: ".all",
    percentPosition: true,
    masonry: {
      columnWidth: ".all"
    }
  });

  // Événement de clic du filtre
  $('.filters_menu li').on('click', function () {
    $('.filters_menu li').removeClass('active');
    $(this).addClass('active');
    var data = $(this).attr('data-filter');
    $grid.isotope({ filter: data });
  });

});
