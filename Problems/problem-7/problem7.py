import math

def isprime(number):
    if number == 1:
        return False
    else:
        if number == 2:
            return True
        else:
            for i in range(2,math.ceil(math.sqrt(number))+1):
                if number % i == 0:
                    return False
            return True

primes = []

i = 1
while True:
    if isprime(i):
        primes.append(i)
    if len(primes) > 10001:
        break
    i += 1

print(primes[10000])
