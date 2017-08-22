triangle = [] # Put input triangle into a list of lists
with open('input.txt') as input:
    for line in input:
        triangle.append(line.strip().split(' '))

for row in triangle:
    print(row)
