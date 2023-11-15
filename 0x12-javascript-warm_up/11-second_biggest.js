#!/usr/bin/node
let x = 0;
if (process.argv.length === 3) {
  console.log('0');
} else if (process.argv) {
  for (let i = 2; i < process.argv.length; i++) {
    if (x < process.argv[i]) {
      x = process.argv[i];
    }
  }
  console.log(x);
} else {
  console.log('0');
}
