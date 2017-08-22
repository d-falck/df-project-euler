import math

# This function reused from numberprinter.py - work out how to import later
def digitsOf(N): # Separates N into a list of its digits
    N = abs(N) # Make positive
    length = math.floor(math.log10(N)) + 1 # How many digits
    separated = []
    separated.append(int(N % 10)) # We build the list in reverse order, starting with the units digit
    for i in range(1,length): # Every digit can be found from N modulo something and the previous digit
        new = int((N % 10**(i+1) - separated[i-1])/(10**i))
        separated.append(new)
    separated.reverse() # Finally, put the list in the right order
    return separated

def factorial(N):
    product = 1
    for i in range(N-1):
        product *= (N-i)
    return product

print(sum(digitsOf(factorial(100))))
