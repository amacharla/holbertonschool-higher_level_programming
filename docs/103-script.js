window.onload = function () {
  const url = 'https://query.yahooapis.com/v1/public/yql?';
  const data = {
    q: 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + $('INPUT#city_search').val() + '")',
    format: 'json'
  };

  $('INPUT#btn_search').submit(function () {
    $.getJSON(url, data, function (data) {
      $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
    });
  });
};
