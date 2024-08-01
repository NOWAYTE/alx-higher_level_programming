#!/usr/bin/node

const request = require('request');

const burl = 'https://swapi-api.alx-tools.com/api/films/';

request.get(burl + process.argv[2], (error, response, body) => {
  if (error) throw error;

  console.log(JSON.parse(body).title);
});
