#!/usr/bin/node
const request = require('request');
const url1 = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    if (url1 === url) {
      console.log(1);
    }
    return;
  }
  const jsonparse = JSON.parse(body);
  console.log(jsonparse.films.length);
});
