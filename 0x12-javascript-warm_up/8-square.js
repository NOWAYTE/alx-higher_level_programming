#!/usr/bin/node
const argv = process.argv.slice(2);
if (!isNaN(parseInt(argv[0]))) {
  for (let i = 0; i < argv[0]; i++) {
    let x = [];
    for (let i = 0; i < argv[0]; i++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
