def ringLength(ringNumber): # Gives how many numbers are in ring indexed ringNumber
    return (1+2*ringNumber)**2 - (1+2*(ringNumber-1))**2 # Square the side length and subtract the square of the previous side length

ring = 1 # The index of the concentric ring of the current number: the central number is ring 0
n = 2 # The current number
indexInRing = 0 # How far through the current ring the number is
diagonalSum = 1
while True:
    if ring > 500:
        break
    length = ringLength(ring)
    if (indexInRing + 1) % (length / 4) == 0: # If 1/4 through the ring (so diagonal)
        diagonalSum += n
    if (indexInRing + 1) == length:
        indexInRing = 0
        ring += 1
    else:
        indexInRing += 1
    n += 1

print(diagonalSum)
