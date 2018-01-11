#!/usr/bin/node
// refer to Onenote regarding `~~`

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
  let occur = {};
  body.map(task => task.completed && (occur[task.userId] = ~~occur[task.userId] + 1));
  console.log(occur);
});
