$.getJSON('https://swapi.co/api/films/?format=json', function (films) {
  $.map(films.results, function (film) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
