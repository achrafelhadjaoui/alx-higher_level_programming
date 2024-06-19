#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  if (numbers.length === 1) {
    console.log(0);
  } else {
    numbers.sort((a, b) => b - a);
    console.log(numbers[1]);
  }
}
