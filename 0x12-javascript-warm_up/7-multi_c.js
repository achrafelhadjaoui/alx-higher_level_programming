#!/usr/bin/node

const { argv } = require('process');

const number = parseInt(argv[2], 10);

if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
