def PathsToPoint(x,y): # This is using basic dynamic programming
    nodes = [[1 for a in range(x)] for b in range(y)] # Matrix containing number of paths to each point
    for i in range(1,x):
        for j in range(1,y):
            nodes[i][j] = nodes[i-1][j] + nodes[i][j-1]
    return nodes[x-1][y-1]

print(PathsToPoint(21 ,21))
