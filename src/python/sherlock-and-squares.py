import math

count = 0
t = int(raw_input().strip())
for val in xrange(t):
    x = map(int, raw_input().strip().split(' '))
    count = 0
    base = math.ceil(math.sqrt(x[0]))
    upper = math.floor(math.sqrt(x[1]))
    print int(upper - base + 1)
