#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) {
  console.log('Not a number');
} else {
  const number = parseInt(argv[2]);
  Number.isInteger(number)
    ? console.log(`My number: ${number}`)
    : console.log('Not a number');
}
