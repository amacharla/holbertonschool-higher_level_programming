#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

if (args < 3) {
  console.log('Need to pass URL and file path as argument');
  process.exit(1);
}

const options = {
  uri: args[0],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) { return console.log(err); }
  fs.writeFile(args[1], body.toString(), 'utf-8', err => {
    if (err) console.log(err);
  });
});
