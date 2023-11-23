#!/usr/bin/node

const args = process.argv.slice(2);

function factorial(n){
	if (isNaN(n) || n < 0){
		return 1;
	}

	if (n === 0){
		return 1;
	}


	return n * factorial(n - 1);
}

const input = args[0];

console.log(factorial(input));
