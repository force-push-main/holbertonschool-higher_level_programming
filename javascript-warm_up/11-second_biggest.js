#!/usr/bin/node

const { argv } = require('node:process');

const raw_arr = argv.slice(2);
const num_arr = raw_arr.map(Number);

// prettier-ignore
function compareNumbers (a, b) {
    return a - b
}

// prettier-ignore
function findSecondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  }
  arr.sort(compareNumbers);
  return arr[arr.length - 2];
}

console.log(findSecondBiggest(num_arr));
