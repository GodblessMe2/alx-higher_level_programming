#!/usr/bin/node
let result = '';
const number = Math.floor(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      result += 'X';
    }
    result += '\n';
  }
  console.log(result);
}
