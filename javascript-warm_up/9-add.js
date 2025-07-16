#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  const int1 = parseInt(a);
  const int2 = parseInt(b);
  const sum = int1 + int2;
  console.log(sum);
}

add(argv[2], argv[3]);
