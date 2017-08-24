largest_pallen = 0
for i in range(100,1000):
    for j in range(i,1000):
        prod = i*j
        digits = [0,0,0,0,0,0] # Separating the product out into its digits
        digits[5] = int(prod % 10)
        digits[4] = int((prod % 100 - digits[5])/10)
        digits[3] = int((prod % 1000 - 10*digits[4])/100)
        digits[2] = int((prod % 10000 - 100*digits[3])/1000)
        digits[1] = int((prod % 100000 - 1000*digits[2])/10000)
        digits[0] = int((prod % 1000000 - 10000*digits[1])/100000)
        if digits[0] == 0:
            if digits[1] == digits[5] and digits[2] == digits[4]:
                if prod > largest_pallen:
                    largest_pallen = prod
        else:
            if digits[0] == digits[5] and digits[1] == digits[4] and digits[2] == digits[3]:
                if prod > largest_pallen:
                    largest_pallen = prod
print(largest_pallen)
