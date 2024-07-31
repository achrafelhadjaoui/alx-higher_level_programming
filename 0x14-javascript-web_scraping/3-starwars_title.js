#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('u need <number>');
  process.exit(1);
}
const number = parseInt(process.argv[2]);

request(`https://swapi-api.alx-tools.com/api/films/${number}`, { json: true }, (err, res, body) => {
  console.error('error:', err); // Print the error if one occurred
  console.log(body.title); // Print the HTML for the Google homepage.
});
