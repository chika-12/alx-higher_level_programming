#!/usr/bin/node
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
const { argv } = require('node:process');
if (argv[2] === '') {
  console.log(1);
} else {
  const number = parseInt(argv[2], 10);
  if (isNaN(number)) {
    console.log(1);
  } else {
    console.log(factorial(number));
  }
}
