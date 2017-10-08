def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
sorted = False
swaps = 0
for j in range(0, len(a)):
    for i in range(0, len(a)-1):
        sorted = True
        if a[i] > a[i+1]:
            swaps += 1
            swap(a, i, i+1)
            sorted = False

print "Array is sorted in %s swaps." % str(swaps)
print "First Element: %s" % str(a[0])
print "Last Element: %s" % str(a[len(a) - 1])