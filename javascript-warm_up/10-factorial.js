#!/usr/bin/node

const { argv } = require('node:process');

// prettier-ignore
function findFactorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 1) {
    return a;
  }
  return a * findFactorial(a - 1);
}

console.log(findFactorial(argv[2]));
