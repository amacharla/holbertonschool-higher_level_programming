#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args < 1) {
  console.log('Need to pass movie id as argument');
  process.exit(1);
}

const options = {
  uri: 'http://swapi.co/api/films/' + args[0],
  method: 'GET',
  json: true
};

