import math

def isPrime(number): # From problem 10
    if number < 0: # Safeguard against negative numbers
        return False
    prime = True #Assume prime
    if number == 1:
        return False
    if number == 2:
            return True
    else:
        for i in range(2,math.ceil(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True

def consecutivePrimes(a,b): # The number of primes for consecutive values of n, starting with n = 0, produced by n^2 + an + b
    n = 0
    while True:
        if isPrime(n**2 + a*n + b):
            n += 1
        else:
            return n

coeffsBelow = 1000
maxConsecutives = 0
product = 0
for a in range(-(coeffsBelow-1),coeffsBelow):
    print(a)
    for b in range(-(coeffsBelow-1),coeffsBelow):
        consecutives = consecutivePrimes(a,b)
        if consecutives > maxConsecutives:
            maxConsecutives = consecutives
            product = a*b

print(product)
