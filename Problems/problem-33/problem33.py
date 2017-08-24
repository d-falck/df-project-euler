import math

def prod(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product

def factorsOf(n): # Simpler version than from problem 12
    factors = set()
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            factors.update([i,int(n/i)])
    return factors

def sharedFactor(A,B): # Returns a shared factor of A and B, or None if there are none
    factorsA = factorsOf(A)
    factorsB = factorsOf(B)
    for factor in factorsA:
        if factor in factorsB and factor != 1:
            return factor
    return None

def lowestTerms(A,B): # Returns the numerator and denominator of the fraction A/B in its lowest terms
    while True:
        shared = sharedFactor(A,B)
        if shared == None:
            return (A,B)
        else:
            A = int(A/shared)
            B = int(B/shared)

def digitsOf(n): # As before
    return(tuple(int(i) for i in str(n)))

def checkSuitable(digitsA,digitsB): # If both have no zeros, are of length 2 and they share a digit, returns the indices of the shared digit
    if len(digitsA) != 2 or len(digitsB) != 2 or 0 in digitsA or 0 in digitsB:
        return (None,None)
    else:
        for i, digit in enumerate(digitsA):
            if digit in digitsB:
                return (i,digitsB.index(digit)) # This implementation works, but might need to come back to include the second pair of indices for numbers like 49,94
        return (None,None)

def isCurious(A,B): # Checks if the fraction A/B is curious
    if A >= B:
        return False
    digitsA = digitsOf(A)
    digitsB = digitsOf(B)
    suitability = checkSuitable(digitsA,digitsB)
    if suitability == (None,None):
        return False
    else:
        cancelled = (digitsA[1 - suitability[0]], digitsB[1 - suitability[1]]) # Remove the duplicate digits
        if A / B == cancelled[0] / cancelled[1]:
            return True

curiouses = set()
for A in range(1,100):
    for B in range(A,100):
        if isCurious(A,B):
            curiouses.add((A,B))

curiousProductFraction = (prod(i[0] for i in curiouses), prod(i[1] for i in curiouses))
simplest = lowestTerms(curiousProductFraction[0],curiousProductFraction[1])
print(simplest[1])
