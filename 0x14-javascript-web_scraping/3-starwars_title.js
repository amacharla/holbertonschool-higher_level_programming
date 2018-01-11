#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args < 1) {
  console.log('Need to pass episode number as argument');
  process.exit(1);
}

const options = {
  uri: 'http://swapi.co/api/films/' + args[0],
  method: 'GET',
  json: true
};

request(options, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.title);
});
