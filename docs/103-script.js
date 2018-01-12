$(function () {
  const url = 'https://query.yahooapis.com/v1/public/yql?';
  const name = $('INPUT#city_search').val();
  const data = {
    q: 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + name + '")',
    format: 'json'
  };

  $('INPUT#btn_search').submit(function () {
    $.getJSON(url, data, function (data) {
      $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
    });
  });
});
