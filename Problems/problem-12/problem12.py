import math

def findFactors(n):
    factors = []
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return factors

def triangularNumber(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

index = 0

while True:
    if len(findFactors(triangularNumber(index))) >= 500:
        print(triangularNumber(index))
        break
    index += 1
