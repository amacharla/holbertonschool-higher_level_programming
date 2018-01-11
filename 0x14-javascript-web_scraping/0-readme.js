#!/usr/bin/node

const args = process.argv.slice(2);
if (args < 1) {
  console.log('Need to pass in file path as argument');
  process.exit(1);
}

const fs = require('fs');

fs.readFile(args[0], 'utf-8', (err, buffer) => {
  if (err) console.log(err);
  else console.log(buffer);
});
