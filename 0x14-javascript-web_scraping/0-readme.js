#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as the first argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file asynchronously
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
