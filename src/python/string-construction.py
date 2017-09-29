#!/bin/python

import sys

def stringConstruction(s):
    # Complete this function

    s_list = list(s)
    alcounts = {}
    for ch in s_list:
        if ch not in alcounts:
            alcounts[ch] = 0

    return len(alcounts.keys())

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = stringConstruction(s)
        print result

