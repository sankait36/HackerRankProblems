def array_left_rotation(a, n, k):
    # k mod n
    index_to_split = 0
    if k == n:
        return a
    else:
        index_to_split = k - 1 
        s1 = a[:k]
        s2 = a[k:]
        return s2+s1
        
    # Logic: Find the point to split, make halved s1 and s2
    # Append s2 to s1, return the final array
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
