#!/bin/python

import sys

def findDist(x,y):
    return abs(x-y)

q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    A_C_dist = findDist(x,z)
    B_C_dist = findDist(y,z)

    if A_C_dist == B_C_dist:
        print "Mouse C"
    elif A_C_dist < B_C_dist:
        print "Cat A"
    else:
        print "Cat B"