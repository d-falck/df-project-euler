with open('input.txt') as f:
    numbers = [int(line.strip()[0:13]) for line in f]

summation = sum(numbers)
first10 = int(str(summation)[0:10])
print(first10)
