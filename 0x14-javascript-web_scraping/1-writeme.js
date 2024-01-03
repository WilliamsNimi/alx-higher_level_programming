#!/usr/bin/node
const file = require('node:fs');
const f_content = process.argv[3];
file.writeFile(process.argv[2], f_content, error => {
    if (error) {
	console.error(error);
    }
});
