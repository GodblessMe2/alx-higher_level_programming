#!/usr/bin/node
const number = Math.floor(process.argv[2]);
const word = 'C is fun';
if (isNaN(number)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < number; i++) {
  console.log(word);
}
