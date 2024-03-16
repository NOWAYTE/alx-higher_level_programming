#!/usr/bin/node
const argv = process.argv.slice(2);
const x = parseInt(argv[0]);
const y = parseInt(argv[1]);

function add (x, y) {
  return x + y;
}

console.log(add(x, y));
