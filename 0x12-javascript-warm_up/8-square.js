#!/usr/bin/node

const args = process.argv.slice(2);
const sz = parseInt(args[0], 10);

if (isNaN(sz)) {
  console.log('Missing size');
} else if (sz <= 0) {
  console.log('Size must be greater than 0');
} else {
  for (let i = 0; i < sz; i++) {
    let row = '';
    for (let j = 0; j < sz; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
