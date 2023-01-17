#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const file = argv[3];
request(url, (error, response, body) => {
  if (error) { 
    console.log('error:', error);
  } else {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) return console.log(err);
    });
  }
});
