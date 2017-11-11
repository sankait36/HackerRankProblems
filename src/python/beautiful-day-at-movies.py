i, j, k = map(int, raw_input().strip().split(' '))

beautiful_days = 0
for x in range (i, j+1):
    #list_x = map(int, reversed(list(str(x)))) 
    #s = map(str, list_x)
    #s = ''.join(s)
    #s = int(s)
    s = int(str(x)[::-1])
    evl = float(abs(x-s))/k
    if evl.is_integer():
        beautiful_days += 1
print beautiful_days

