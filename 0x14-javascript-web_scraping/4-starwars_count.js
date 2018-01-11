#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args < 1) {
  console.log('Need to pass URL as argument');
  process.exit(1);
}

const options = {
  uri: args[0],
  method: 'GET',
  json: true
};

request(options, (err, res, body) => {
  if (err) { return console.log(err); }
  let count = 0;
  body.results.map(film => film.characters.map(charc => charc.endsWith('/18/') && count++));
  console.log(count);
});
