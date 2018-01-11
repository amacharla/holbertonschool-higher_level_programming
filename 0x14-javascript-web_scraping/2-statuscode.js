#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args < 1) {
  console.log('Need to pass URL as argument');
  process.exit(1);
}

request(args[0], (err, res) => {
  if (err) console.log(err);
  else console.log('code:', res.statusCode);
});
