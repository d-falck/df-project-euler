sequence = set()

for i in range(2,101):
    for j in range(i,101):
        sequence.add(i**j)
        sequence.add(j**i)

print(len(sequence))
