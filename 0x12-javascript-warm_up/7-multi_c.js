#!/usr/bin/node
for (let i = 0; i < process.argv[2]; i++) console.log('C is fun');
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
