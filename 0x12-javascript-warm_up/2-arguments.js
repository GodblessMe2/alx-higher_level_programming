#!/usr/bin/node
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv.length === 3 ? 'Argument found' : 'Argument found');
