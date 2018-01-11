#!/usr/bin/node

const args = process.argv.slice(2);
if (args < 1) {
  console.log('Need to pass in file path as argument');
  process.exit(1);
}

const fs = require('fs');
fs.writeFile(args[0], args[1], 'utf-8', err => {
  if (err) console.log(err);
});
