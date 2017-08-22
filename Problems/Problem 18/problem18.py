triangle = [] # Put input triangle into a list of lists
with open('input.txt') as input:
    for line in input:
        triangle.append(line.strip().split(' '))

maxsum = [[0 for entry in row] for row in triangle] # Zeroes same size as triangle

for i, row in enumerate(triangle):
    for j, entry in enumerate(row):
        if i == 0:
            maxsum[i][j] = entry
        if j == 0: # If at the start of the line, only one option for max sum
            maxsum[i][j] = entry + maxsum[i-1][j]
        elif j == len(row) - 1: # If at the end of the line, only one option
            maxsum[i][j] = entry + maxsum[i-1][j-1]
        else: # Normally, compare the two numbers directly above entry and add the largest to the maxsum here
            if maxsum[i-1][j-1] > maxsum[i-1][j]:
                maxsum[i][j] = entry + maxsum[i-1][j-1]
            else:
                maxsum[i][j] = entry + maxsum[i-1][j]
