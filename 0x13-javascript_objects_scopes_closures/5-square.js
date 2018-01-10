#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (length) {
    super(length, length);
  }
}

module.exports = Square;
