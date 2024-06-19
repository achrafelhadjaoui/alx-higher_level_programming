#!/usr/bin/node

const { argv } = require('process');

const number = parseInt(argv[2]);
Number.isInteger(number)
   ? number.map((item) => {
	console.log('item')
});
   : console.log('Missing number of occurrences');;
