#!/bin/python

import sys

def lonely_integer(a):
    counts = {}
    for num in a:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    for key in counts:
        if counts[key] == 1:
            return key
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
