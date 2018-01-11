#!/usr/bin/node

const request = require('request');

const options = {
  uri: 'http://swapi.co/api/people/18',
  method: 'GET',
  json: true
};

request(options, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.films.length);
});
