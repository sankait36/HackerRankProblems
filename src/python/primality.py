def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while (i*i) <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    prime = isPrime(n)
    if prime:
        print "Prime"
    else:
        print "Not prime"