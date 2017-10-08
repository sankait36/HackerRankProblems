n = input()
ar = [int(i) for i in raw_input().strip().split()]

ar.sort()
mid = n/2
print ar[mid]