#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length > 2) {
  argv.forEach((val, index) => {
    if (index > 1) {
      console.log('Argument found');
    }
  });
} else {
  console.log('No argument');
}
