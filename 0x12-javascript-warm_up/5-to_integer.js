#!/usr/bin/node

const { argv } = require('node:process');

if (parseInt(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
