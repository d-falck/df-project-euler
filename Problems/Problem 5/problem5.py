smallest_multiple = 0
number = 20
i = number
while True:
    for j in range(number,0,-1):
        if i % j != 0:
            i += number
            break
        if j == 1: # If checked all of them and still here
            smallest_multiple = i
            break
    if smallest_multiple != 0:
        break
print(smallest_multiple)
