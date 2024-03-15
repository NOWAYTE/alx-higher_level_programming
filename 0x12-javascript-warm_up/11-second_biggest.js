#!/usr/bin/node

const argv = process.argv.slice(2).map(arg => parseInt(arg));

if (argv.length === 0 || argv.length === 1) {
  console.log(0);
} else {
  const sorted = argv.sort((a, b) => b - a);

  if (sorted[1] === sorted[0]) {
    console.log(sorted[2]);
  } else {
    console.log(sorted[1]);
  }
}
