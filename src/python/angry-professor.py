#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    in_class = 0
    for vals in a:
        if vals <= 0:
            in_class += 1
    if in_class < k:
        print "YES"
    else:
        print "NO"