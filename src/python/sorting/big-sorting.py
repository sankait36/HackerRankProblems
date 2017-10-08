#!/bin/python

import sys

def comparator(a, b):
    if len(a) == len(b):
        if a < b:
            return -1
        else:
            return 1
    if len(a) < len(b):
        return -1
    else:
        return 1

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here
unsorted.sort(cmp=comparator)
for data in unsorted:
    print data