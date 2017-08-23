# We do long division on the number: we know that the repetend starts when there's a remainder of 1 and ends when there's a remainder we've seen before

def reciprocalPeriod(n):
    inRepetend = False # This is true when we're in the middle of the repeating secion of the decimal
    length = 0 # Current length of the repetend
    remainder = 1 % n # Remainder from current place
    pastRemainders = [remainder] # Past remainders
    while True:
        #print(remainder)
        if inRepetend:
            if remainder in pastRemainders: # The repetend ends when we get a remainder we've had before
                inRepetend = False
                return length
        else:
            if remainder == 1: # The repetend starts with remainder 1
                inRepetend = True
        if remainder == 0: # If terminating
            return 0
        pastRemainders.append(remainder)
        if inRepetend:
            length += 1
        remainder = (10*remainder) % n

maxLength = 0
maxLengthNumber = 0
for d in range(2,1000):
    period = reciprocalPeriod(d)
    if period > maxLength:
        maxLength = period
        maxLengthNumber = d

print(maxLengthNumber)
