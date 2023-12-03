#!/usr/bin/node
let x = [];
if (process.argv.length === 3) {
  console.log('0');
} else if (process.argv) {
  x = process.argv.sort();
  console.log(x[process.argv.length - 2]);
} else {
  console.log('0');
}
