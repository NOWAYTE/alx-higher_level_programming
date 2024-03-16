#!/usr/bin/node
const argv = process.argv.slice(2)
let x = parseInt(argv[0]);
let y = parseInt(argv[1]);

function add(x, y) {
	return x + y;
}

console.log(add(x, y));
