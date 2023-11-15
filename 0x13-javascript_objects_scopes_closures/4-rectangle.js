#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w !== 0 && h !== 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        console.log('X');
      }
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
