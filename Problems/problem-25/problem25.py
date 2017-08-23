import math

# Terms A and B are always the last two terms in the sequence

termA = 1
termB = 1
i = 3
while True:
    currentTerm = termA + termB
    if math.floor(math.log10(currentTerm)) + 1 >= 1000: # If more than 999 digits
        break
    termA = termB
    termB = currentTerm
    i += 1

print(i)
