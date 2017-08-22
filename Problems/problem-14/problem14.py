def nextCollatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

def CollatzSequence(n):
    sequence = []
    sequence.append(n)
    while True:
        n = nextCollatz(n)
        sequence.append(n)
        if n == 1:
            break
    return sequence

def longestCollatz(cap): # Returns the number below 'cap' which generates the longest Collatz sequence, and its length
    longest = 0
    for i in range(cap-1,1,-1):
        length = len(CollatzSequence(i))
        if length > longest:
            longest = length
            longestat = i
    return [longestat,longest]

print(longestCollatz(1000000))
