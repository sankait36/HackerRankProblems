#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

i = 0
jumps = 0
while i < n-1:
    if i + 2 >= n:
        i = i + 1
    else:
        if c[i+2] == 0:
            i = i + 2
        else:
            i = i + 1
    jumps += 1

print jumps