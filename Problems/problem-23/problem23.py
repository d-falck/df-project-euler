import math

def properDivisors(n): # Ported roughly from problem 12
    factors = []
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i not in factors and i < n:
                factors.append(i)
            if int(n/i) not in factors and int(n/i) < n:
                factors.append(int(n/i))
    return factors

def isAbundant(N): # Checks if N is an abundant number
    if sum(properDivisors(N)) > N:
        return True
    else:
        return False

checkBelow = 28123

abundants = []
for i in range(1,checkBelow+1):
    if isAbundant(i):
        abundants.append(i)

# We now have all the abundant numbers under checkBelow in the list abundants

abundantSums = []
for abundant1 in abundants:
    for abundant2 in abundants:
        if abundant1 + abundant2 not in abundantSums:
            abundantSums.append(abundant1 + abundant2)

print(abundantSums)
