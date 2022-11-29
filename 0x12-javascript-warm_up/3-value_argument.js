#!/usr/bin/node
const count = process.argv;
console.log(count.length === 2 ? 'No argument' : count[2]);
