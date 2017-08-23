# This one can be done on paper.
# 10! = 3.7m permutations overall, 9! = 370,000 perms of the last 9 digits
# So, floor(1m/370,000)  = 2 is the number of starting digits whose permutations have been exhausted before we reach the millionth
# Hence we know the first digit will be not 0 or 1 but 2
# We repeat this recursively (ah, some programming!).

import math

position = 1000000 # the permutation number we care about (indexed from 1)
used = 0
digits = [0 for i in range(10)]
remainingDigits = [0,1,2,3,4,5,6,7,8,9]
noOfTimes = 1

# firstDigit = math.floor(position/math.factorial(9))
# secondDigit = math.floor((position-math.factorial(9))/math.factorial(8))
for i in range(9,-1,-1):
    noOfTimes = math.floor((position-1 - used) / math.factorial(i))
    digits[9-i] = remainingDigits[noOfTimes]
    remainingDigits.remove(digits[9-i])
    used += noOfTimes*math.factorial(i)

print(digits)
