#!/usr/bin/node
let squareStr = '';
if (typeof (parseInt(process.argv[2])) === 'number') {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    squareStr += 'X';
  }
  for (let j = 0; j < parseInt(process.argv[2]); j++) {
    console.log(squareStr);
  }
} else {
  console.log('Missing size');
}
