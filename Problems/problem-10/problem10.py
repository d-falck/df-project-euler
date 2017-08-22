import math

def isPrime(number):
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

def sumOfPrimes(N): # Sum of all primes below N
    sum = 2
    for i in range(3,N+1,2):
        if isPrime(i):
            sum += i
    return sum

print(sumOfPrimes(2000000))
