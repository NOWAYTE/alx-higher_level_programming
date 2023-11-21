#!/usr/bin/node

const args = process.argv.slice(2);

let num1 = parseInt(args[0]);
let num2 = parseInt(args[1]);

function add(a, b){
	return a + b;
}

sum = add(num1, num2);

console.log(`${sum}`);
