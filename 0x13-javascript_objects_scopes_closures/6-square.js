#!/usr/bin/node
const PrevSquare = require('./5-square');
class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c || 'X';
    for (let n = 0; n < this.height; n++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write(myChar);
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
