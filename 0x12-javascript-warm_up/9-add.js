#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const num1 = Math.floor(process.argv[2]);
const num2 = Math.floor(process.argv[3]);
add(num1, num2);
