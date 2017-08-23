import math

# Reused function
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

totalSum = 0
i = 1
while True:
    if i % 10000 == 0:
        print(i)
    digits = digitsOf(i)
    powerSum = sum(j**5 for j in digits)
    if i == powerSum:
        totalSum += i
    if i == 10000000:
        break
    i += 1

print(totalSum)
