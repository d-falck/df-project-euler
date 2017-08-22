import math

def digits(N):
    length = math.floor(math.log10(N)) + 1 # How many digits
    separated = []
    separated.append(int(N % 10))
    for i in range(1,length):
        new = int((N % 10**(i+1) - separated[i-1])/(10**i))
        separated.append(new)
    separated.reverse()
    return separated

print(sum(digits(2**1000)))
