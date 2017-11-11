# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
d = {}
for val in xrange(n):
    k, v = raw_input().strip().split(' ')
    if k not in d:
        d[k] = ''
    d[k] = v
    
for val in xrange(n):
    find = raw_input().strip()
    if find in d:
        print "%s=%s" % (find, d[find])
    else:
        print "Not found"