#!/usr/bin/node
if (typeof (parseInt(process.argv[2])) === 'number') {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
