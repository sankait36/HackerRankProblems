#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    num_lst = map(int, str(n))
    count = 0
    for num in num_lst:
        if num != 0:
            if n % num == 0:
                count += 1
    print count