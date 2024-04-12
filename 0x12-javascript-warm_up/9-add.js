#!/usr/bin/node

const Integer = parseInt(process.argv[2], 10);
const Integer1 = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}

console.log(add(Integer, Integer1));
