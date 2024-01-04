#!/usr/bin/node
const file = require('fs');
const Fcontent = process.argv[3];
file.writeFile(process.argv[2], Fcontent, error => {
  if (error) {
    console.error(error);
  }
});
