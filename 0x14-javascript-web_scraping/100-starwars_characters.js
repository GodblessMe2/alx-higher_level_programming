#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, (error, response, body) {
  if (!error) {
    const data = JSON.parse(body).characters;
    data.array.forEach(dataResponse => {
      request(dataResponse, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
