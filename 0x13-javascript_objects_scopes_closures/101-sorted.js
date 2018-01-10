#!/usr/bin/node

let dict = require('./101-data').dict;
let keys = new Set(...dict.values());
let newdict = {};

for (let value in keys) {
  newdict[value] = (dict.entries()) => { return
}
