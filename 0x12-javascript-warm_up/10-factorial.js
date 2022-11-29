#!/usr/bin/node
function factorial (num) {
  let fact = 1;
  for (let i = 1; i <= num; i++) {
    fact = fact * i;
  }
  console.log(fact);
}
const number = Math.floor(process.argv[2]);
factorial(number);
