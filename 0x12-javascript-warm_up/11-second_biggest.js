#!/usr/bin/node
/**
 * Searching for the second biggest integer
 */
const { argv } = require('node:process');
let index;
let largest = 0;
let second = 0;
for (index = 2; index < argv.length; index++) {
  const num = parseInt(argv[index]);
  if (num > largest) {
    second = largest;
    largest = num;
  } else if (num > second && num < largest) {
    second = num;
  }
}
console.log(second);
