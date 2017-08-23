def prod(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product

with open('input.txt') as f:
    data = f.read().replace('\n','')

digitsLength = 13 # The number of adjacent digits we want to find the product of
maxProduct = 0

for i in range(len(data)-digitsLength):
    digits = [int(j) for j in data[i:i+digitsLength]]
    product = prod(digits)
    if product > maxProduct:
        maxProduct = product

print(maxProduct)
