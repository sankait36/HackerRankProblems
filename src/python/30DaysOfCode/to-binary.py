#!/bin/python

import sys

n = int(raw_input().strip())
counter = 0
max_ones = 0
while n > 0:
    remainder = n % 2
    n = n/2
    if remainder == 1:
        counter += 1
        if counter > max_ones:
            max_ones = counter
    else:
        counter = 0


print max_ones
