#!/usr/bin/node
const request = require('request');
const files = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  files.writeFile(filename, body, error => {
    if (error) {
      console.error(error);
    }
  });
});
