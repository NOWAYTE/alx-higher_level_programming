#!/usr/bin/node

const args = process.argv.slice(2);

const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

function add (a, b) {
  return a + b;
}

const sum = add(num1, num2);

console.log(`${sum}`);