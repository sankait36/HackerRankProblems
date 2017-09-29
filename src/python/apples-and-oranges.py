#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

apple_count = 0
orange_count = 0

for ap in apple:
    if (a + ap) >= s and (a + ap) <= t:
        apple_count += 1

for org in orange:
    if (b + org) <= t and (b + org) >= s:
        orange_count += 1

print apple_count
print orange_count