#!/usr/bin/node
let n = parseInt(process.argv[2]);
if (process.argv[2] === undefined) console.log('Missing size');
for (let i = 0; i < n; i++) console.log('X'.repeat(n));
