fibonacci = [0,0,0]
fibonacci[0] = 0
fibonacci[1] = 1
fibonacci[2] = 1
summation = 0
for i in range(3,4000000000):
    fibonacci.append(0)
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    if fibonacci[i] >= 4000000:
        break
    if fibonacci[i] % 2 == 0:
        summation += fibonacci[i]
print(summation)
