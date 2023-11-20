#!/usr/bin/node

const args = process.argv.slice(2);

let square = '';

if (Number.isInteger(Number(args[0]))) {
  for (let i = 0; i < args[0]; i++) {
    for (let j = 0; j < args[0]; j++) {
      square += 'X';
    }

    square += '\n';
  }

  console.log(square);
} else {
  console.log('Missing size');
}
