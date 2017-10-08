#!/bin/python
def count(ar, m):
    counts = {}
    for x in range(0, 100):
        if x not in counts:
            counts[x] = 0
    for n in ar:
        if n in counts:
            counts[n] += 1

    res = []
    for key in counts:
        for y in range(0, counts[key]):
            res.append(key)

    sarr = [str(a) for a in res]
    print ' '.join(sarr)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
count(ar, m)
