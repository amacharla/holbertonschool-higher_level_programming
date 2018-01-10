#!/usr/bin/node

let exec = require('child_process').exec;
let args = process.argv.slice(2);
if (args < 3) process.exit(1);

function child () { exec('cat', args[1], args[2], '>', args[3]); }
child();
