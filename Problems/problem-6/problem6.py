def sumofsquares(n):
    return n*(n+1)*(2*n+1)/6

def sumofintegers(n):
    return n*(n+1)/2

def specialdifference(n): # Finds the difference between the sum of squares and the square sum up to n
    return abs(sumofsquares(n) - (sumofintegers(n))**2)

print(specialdifference(100))
