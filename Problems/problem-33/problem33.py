def digitsOf(n): # As before
    return(tuple(int(i) for i in str(n)))

def areSuitable(a,b): # Returns true if a and b are two-digit numbers and share a digit
    digitsA = digitsOf(a)
    digitsB = digitsOf(b)
    if len(digitsA) != 2 or len(digitsB) != 2:
        return False
    else:
        for digit in digitsA:
            if digit != 0 and digit in digitsB:
                return True
        return False

print(areSuitable(54,48))
