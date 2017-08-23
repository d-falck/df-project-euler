def prod(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product

with open('input.txt') as f:
    grid = [[int(i) for i in line.replace('\n','').split(' ')] for line in f]

width = len(grid[0])
height = len(grid)

maxProduct = 0
adjacents = 4

# Vertical adjacents
for i in range(height - adjacents + 1):
    for j in range(width):
        product = prod([grid[i+k][j] for k in range(adjacents)])
        if product > maxProduct:
            maxProduct = product

# Horizontal adjacents
for i in range(height):
    for j in range(width - adjacents + 1):
        product = prod([grid[i][j+k] for k in range(adjacents)])
        if product > maxProduct:
            maxProduct = product

# Diagonal adjacents
for i in range(height - adjacents + 1):
    for j in range(width - adjacents + 1):
        product = prod([grid[i+k][j+k] for k in range(adjacents)])
        if product > maxProduct:
            maxProduct = product

print(maxProduct)
