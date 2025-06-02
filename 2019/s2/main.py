import math

primes = set()
nprime = set()
def isprime(n):
    if n in nprime:
        return False
    if n in primes:
        return True
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if (n/i).is_integer():
            nprime.add(n)
            return False
    primes.add(n)
    return True
t = int(input())
for j in range(t):
    n = int(input())*2
    for i in range(2, n):
        if isprime(i):
            if isprime(n-i):
                print(n-i, i)
                break
