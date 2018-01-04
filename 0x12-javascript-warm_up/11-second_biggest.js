#!/usr/bin/node
if (process.argv.length <= 3) console.log('0');
else {
  let numarray = process.argv.slice(2);
  let max = Math.max.apply(null, numarray);
  let maxidx = numarray.indexOf(String(max));
  numarray[maxidx] = -Infinity;
  console.log(Math.max.apply(null, numarray));
}
