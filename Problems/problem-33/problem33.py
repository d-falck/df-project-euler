def digitsOf(n): # As before
    return(tuple(int(i) for i in str(n)))

def areSuitable(digitsA,digitsB): # Returns true if both have no zeros, are of length 2 and they share a digit
    if len(digitsA) != 2 or len(digitsB) != 2 or 0 in digitsA or 0 in digitsB:
        return False
    else:
        for digit in digitsA:
            if digit in digitsB:
                return True
        return False

print(areSuitable(54,48))
