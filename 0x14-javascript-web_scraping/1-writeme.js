#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as the first argument
if (process.argv.length !== 4) {
  console.log('Usage: ./0-readme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Get the file path from the command line arguments
const filePath = process.argv[2];
const text = process.argv[3];

// Read the file asynchronously
fs.writeFile(filePath, text, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
