fibonacci = [0,0]
fibonacci[0] = 1
fibonacci[1] = 2
summation = 0
i = 2
while True:
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if fibonacci[i] >= 4000000:
        break
    if fibonacci[i] % 2 == 0:
        summation += fibonacci[i]
    i += 1
print(summation)
