import math

def findFactors(n): # Ported roughly from problem 12
    factors = []
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
            if int(n/i) not in factors:
                factors.append(int(n/i))
    return factors

allFactors = [0]

for i in range(1,10001): # so that allFactors[N] is the list of factors of N
    allFactors.append(findFactors(i))
print(allFactors)

for entry in allFactors:
