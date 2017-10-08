#!/bin/python
def count(ar_num, ar_str, m):
    counts = {}

    for x in range(0, 100):
        if x not in counts:
            counts[x] = 0
    for n in ar_num:
        if n in counts:
            counts[n] += 1
            
    res = []
    for key in counts:
        for y in range(0, counts[key]):
            if str(key) in ar_str:
                res.append(ar_str[str(key)][y])
            

    print ' '.join(res)

m = input()
orig_num = []
orig_str = {}
half = m/2

for x in range(0, m):
    s,t = raw_input().strip().split(' ')
    orig_num.append(int(s))
    if s not in orig_str:
        orig_str[s] = []
    if x < half:
        orig_str[s].append('-')
    else:
        orig_str[s].append(t)

count(orig_num, orig_str, m)