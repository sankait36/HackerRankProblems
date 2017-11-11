#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here

max_h = max(height)
if max_h > k:
    print (max_h - k)
else:
    print 0