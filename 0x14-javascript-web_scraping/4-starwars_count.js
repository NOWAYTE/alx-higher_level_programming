#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) throw error;

  const data = JSON.parse(body);

  data.results.forEach((f) => {
    f.characters.forEach((c) => {
      if (c.includes(18)) {
        count += 1;
      }
    });
  });

  console.log(count);
});
