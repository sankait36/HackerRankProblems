#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

i = 0
E = 100
first_run = True

while i != 0 or first_run:
    i = (i+k) % n # Current cloud
    if c[i] == 0:
        E = E - 1
    else:
        E = E - 3
    first_run = False

print E
