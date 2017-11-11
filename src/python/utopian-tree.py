import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    if n != 0:
        for x in range(1, n+1):
            if x % 2 != 0: # Index 1,3, so on are spring cycles
                h *= 2
            else: # Even indices are 
                h += 1
    print h