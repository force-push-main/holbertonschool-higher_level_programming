#!/usr/bin/node

const { argv } = require('node:process');

function add(a, b) {
  int1 = parseInt(a);
  int2 = parseInt(b);
  //   if (isNaN(a) || isNaN(b)) {
  //     console.log('NaN');
  //     return;
  //   }
  const sum = int1 + int2;
  console.log(sum);
}

add(argv[2], argv[3]);
