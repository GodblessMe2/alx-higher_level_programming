#!/usr/bin/node
const number = Math.floor(process.argv[2]);
console.log(isNaN(number) ? 'Not a number' : `My number: ${number}`);
