#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    const obj = JSON.parse(body).results;
    for (const key of obj) {
      for (const charac of key.characters) {
        if (charac.search('/18') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
