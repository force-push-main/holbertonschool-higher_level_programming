#!/bin/bash

filename=$(ls -1 | grep ^'[0-9]' | sort -V | tail -n 1)
prevNum=${filename%-answer.txt}
newNum=$((prevNum + 1))
cp $filename "${newNum}-answer.txt"
code "${newNum}-answer.txt"