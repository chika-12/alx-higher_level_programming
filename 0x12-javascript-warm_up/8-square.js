#!/usr/bin/node
/**
 * A program to draw a square
 */
const { argv } = require('node:process');
const number = parseInt(argv[2], 10);
let index;
let idx;
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (index = 0; index < number; index++) {
    for (idx = 0; idx < number; idx++) {
      process.stdout.write('X');
    }
    if (index !== number) {
      process.stdout.write('\n');
    }
  }
}
