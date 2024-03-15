#!/usr/bin/node
const argv = process.argv.slice(2);
const x = parseInt(argv[0]);
const y = parseInt(argv[1]);

if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  const z = x + y;
  console.log(z);
}
