d_table = {} # Memoize entries to speed up lookup times

def davis(n):
    if n == 1:
        return d_table[1]
    elif n == 2:
        return d_table[2]
    elif n == 3:
        return d_table[3]
    else:
        if n not in d_table:
            d_table[n] = davis(n-1) + davis(n-2) + davis(n-3)
        return d_table[n]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    d_table[1] = 1
    d_table[2] = 2
    d_table[3] = 4
    print davis(n)
