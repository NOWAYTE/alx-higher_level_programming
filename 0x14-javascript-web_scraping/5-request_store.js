#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], 'utf8', (error, response, body) => {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, (error) => {
    if (error) throw error;
  });
});
