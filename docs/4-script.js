$('DIV#toggle_header').click(function () {
  $(this).css('color', '#FF0000');
  $('header').toggleClass('red green');
});
