#!/usr/bin/node
const request = require('request');
const files = require('fs');
const url = process.argv[2];
let comp = {};
const filename = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
    jsonBody = JSON.parse(body);
    for (let i = 0; i < jsonBody.length; i++){
	for (text in jsonBody[i]){
	}
    }
});
