#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('u need <link>');
  process.exit(1);
}
const link = process.argv[2];
request(link, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
