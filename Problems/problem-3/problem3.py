import math

def isprime(number):
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

def primefactors(number):
    primefactors = []
    keep_going = True
    while keep_going:
        keep_going = False
        for i in range(1,math.ceil(math.sqrt(number))+1): # Only check up to the square root: any other factors can be found from the existing ones
            if number % i == 0:
                if isprime(i):
                    primefactors.append(i)
                    number = number/i
                    keep_going = True
                    break
        if isprime(number):
            primefactors.append(number)
            break
    return primefactors

print(max(primefactors(600851475143)))
