import math

def digitsOf(n): # New, simpler digitsOf function, returns tuple
    return(tuple(int(i) for i in str(n)))

def factorPairs(n): # Returns a set of factor pairs (each represented as a tuple)
    factors = set()
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            factors.add(tuple(sorted([i,int(n/i)])))
    return factors

def productDigits(n): # Returns a set tuples of the digits contained in the multiplicand/multiplier/product identity for n
    container = set()
    pairs = factorPairs(n)
    for pair in pairs:
        digits = digitsOf(pair[0]) + digitsOf(pair[1]) + digitsOf(n) # Combine the tuples
        container.add(digits)
    return container

def isPandigital(digits):
    used = [0] # We're not allowed to count the digit 0
    for digit in digits:
        if digit in used:
            return False
        else:
            used.append(digit)
    return True

def isAcceptable(n): # Returns true if any of the M/M/P identities for n are pandigital 1-9; else returns false
    allDigits = productDigits(n)
    for digits in allDigits:
        if isPandigital(digits) and len(digits) == 9:
            return True
    return False

acceptableSum = 0
for i in range(1,10000):
    if isAcceptable(i):
        acceptableSum += i
print(acceptableSum)
