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

checkUnder = 10000

factorSums = [0 for i in range(checkUnder)]
amicables = []

for i in range(1,checkUnder): # so that factorSums[N] is the sum of proper divisors of N
    # print(i)
    factorSums[i] = sum(properDivisors(i))

for i in range(1,checkUnder):
    # print(i)
    for j in range(1,checkUnder):
        if factorSums[i] == j and factorSums[j] == i and i != j:
            if i not in amicables or j not in amicables:
                amicables.append(i)
                amicables.append(j)

print(amicables)
print(sum(amicables))
