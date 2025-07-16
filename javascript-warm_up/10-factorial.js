#!/usr/bin/node

const { argv } = require('node:process');

const findFactorial = (a) => {
  if (isNaN(a)) {
    return NaN;
  }
  if (a === 1) {
    return a;
  }
  return a * findFactorial(a - 1);
};

const factorial = findFactorial(argv[2]);
if (factorial === 1) {
  console.log(NaN);
} else {
  console.log(findFactorial(argv[2]));
}
