alpha = 'abcdefghijklmnopqrstuvwxyz'
alcounts = {}
alpha_list = list(alpha)
for c in alpha_list:
    alcounts[c] = 0

s = raw_input().strip().replace(' ', '')
list_s = list(s)

for c in list_s:
    alcounts[str.lower(c)] += 1

pangram = True
for c in alcounts:
    if alcounts[c] < 1 :
        pangram = False

if pangram:
    print "pangram"
else:
    print "not pangram"
        