#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  return (a + b);
}

if (argv.length <= 3) {
  console.log('NaN');
} else {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
}
