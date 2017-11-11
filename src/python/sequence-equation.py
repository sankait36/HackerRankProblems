def find_key(p, val):
    for key in p:
        if p[key] == val:
            return key


n = int(raw_input().strip())
x = raw_input().strip().split(' ')

p = {}
for y in range(0, len(x)):
    p[y+1] = int(x[y])

for y in range(1, n+1):
    k = find_key(p, y)
    r_k = find_key(p, k)
    print r_k