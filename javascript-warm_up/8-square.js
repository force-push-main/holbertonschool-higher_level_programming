#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Missing size');
}

for (let i = 0; i < argv[2]; i++) {
  let row = '';
  for (let j = 0; j < argv[2]; j++) {
    row += 'X';
  }
  console.log(row);
}
