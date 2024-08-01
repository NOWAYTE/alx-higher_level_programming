#!/usr/bin/node

const request = require('request');
const i = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${i}`;

request.get(url, (error, response, body) => {
  if (error) throw error;

  const content = JSON.parse(body);
  const chac = content.characters;
  for (const ch of chac) {
    request.get(ch, (error, response, body) => {
      if (error) throw error;
      const n = JSON.parse(body);
      console.log(n.name);
    });
  }
});
