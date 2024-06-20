#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2], 10);
let index;
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (index = 0; index < number; index++) {
    console.log('C is fun');
  }
}
