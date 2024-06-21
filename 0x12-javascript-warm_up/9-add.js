#!/usr/bin/node
/**
 * A script to add numbers
 */
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
const { argv } = require('node:process');
const num1 = parseInt(argv[2], 10);
const num2 = parseInt(argv[3], 10);
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
