#!/bin/python
def partition(ar):    
    left = []
    right = []
    for n in ar:
        if n < ar[0]:
            left.append(n)
        else:
            right.append(n)
    
    res = left + right
    sarr = [str(a) for a in res]
    print ' '.join(sarr)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
