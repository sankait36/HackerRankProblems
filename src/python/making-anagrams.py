def number_needed(a, b):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    alcounts = {}
    for ch in alphas:
        if ch not in alcounts:
            alcounts[ch] = 0
    
    for ch in a:
        alcounts[ch] += 1
    for ch in b:
        alcounts[ch] -= 1
    count = 0

    for key in alcounts:
        count += abs(alcounts[key])
    
    return count
        

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
