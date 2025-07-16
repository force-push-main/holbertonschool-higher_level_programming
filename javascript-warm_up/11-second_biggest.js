#!/usr/bin/node

const { argv } = require('node:process');

const arr = argv.slice(2);

// prettier-ignore
function findSecondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  }
  arr.sort();
  return arr[arr.length - 2];
}

console.log(findSecondBiggest(arr));
