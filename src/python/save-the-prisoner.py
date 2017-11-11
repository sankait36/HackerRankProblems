#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    r = m % n - 1
    if s == 1:
        if r < 0:
            return n
        else:
            return r + 1

    else:
        if r < 0:
            return s - 1
        else:
            x = r + 1 + (s-1)
            if x > n:
                return x % n
            else:
                return x

    # This also works ((M - 1) + (S - 1)) % N + 1;


t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

