#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) throw error;

  console.log('code:', response.statusCode);
});
