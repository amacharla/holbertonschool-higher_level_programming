#!/usr/bin/node

exports.esrever = function (list) {
  if (list === undefined) return 0;
  let reverse = [];
  list.forEach(element => { reverse.unshift(element); });
  return reverse;
};
