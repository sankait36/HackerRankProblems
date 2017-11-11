#!/bin/python

import sys

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0
if y1 > y2: # Do this first since the formula had edge cases
    fine = 10000
else:
    # Convert both to single timestamps to compare
    actual = d1 + m1*31 + y1*365
    expected = d2 + m2*31 + y2*365

    fine = 0
    if actual > expected:
        if y1 == y2:
            if m1 == m2:
                fine = abs(d2-d1)*15
            else:
                fine = abs(m2-m1)*500
        else:
            fine = 10000

print int(fine)

