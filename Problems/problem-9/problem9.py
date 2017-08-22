def PythagoreanTriple(N): # Generates a pythagorean triple that sums to N
    for x in range(1,N+1):
        for y in range(x+1,N+1):
            z = y + 1
            while z*z < x*x + y*y:
                z += 1
            if z*z == x*x + y*y and x+y+z == N:
                return [x,y,z]
    return 'Failed'

print(PythagoreanTriple(1000))
