#!/usr/bin/node
const number = Math.floor(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let result = '';
    for (let j = 0; j < number; j++) result += 'X';
    console.log(result);
  }
}
