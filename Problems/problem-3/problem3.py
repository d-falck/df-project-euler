import math

def isPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(number))+1):
            if number % i == 0:
                return False
    return True

def primeFactors(number):
    primefactors = []
    while True:
        if isPrime(number):
            primefactors.append(number)
            break
        for i in range(1,math.ceil(math.sqrt(number))+1): # Only check up to the square root: any other factors can be found from the existing ones
            if number % i == 0 and isPrime(i):
                primefactors.append(i)
                number = int(number/i)
                break
    return primefactors

print(max(primeFactors(600851475143)))
