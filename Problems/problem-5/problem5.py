smallest_multiple = 0
i = 20
while True:
    for j in range(19,0,-1):
        if i % j != 0:
            i += 20
            break
        if j == 1: # If checked all of them and still here
            smallest_multiple = i
            break
    if smallest_multiple != 0:
        break
print(smallest_multiple)
