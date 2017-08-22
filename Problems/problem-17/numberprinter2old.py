import math

def digitsOf(N): # Separates N into a list of its digits
    length = math.floor(math.log10(N)) + 1 # How many digits
    separated = []
    separated.append(int(N % 10)) # We build the list in reverse order, starting with the units digit
    for i in range(1,length): # Every digit can be found from N modulo something and the previous digit
        new = int((N % 10**(i+1) - separated[i-1])/(10**i))
        separated.append(new)
    separated.reverse() # Finally, put the list in the right order
    return separated

def inWords(N): # Returns the English words for N
    def hundreds(digits): # Deals with triplets of digits
        def units(digit): # Deals with single digits
            digitNames = ['zero','one','two','three','four','five','six','seven','eight','nine']
            return digitNames[digit]

        def tens(digits): # Deals with pairs of digits
            if digits[0] == 0: # If there's a leading zero, pass to the units function
                return units(digits[1])
            elif digits[0] == 1: # If the number is in the teens
                teenNames = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
                return teensNames[digits[1]]
            else: # For any number higher than 19
                tensNames = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
                firstWord = tensNames[digits[0]-2]
                if digits[1] == 0: # If a multiple of 10, just return the first word
                    return firstWord
                else: # Otherwise, concatenate the tens digit with the units digit
                    return '{}-{}'.format(firstWord,units(digits[1]))

        if digits[0] == 0: # If a leading zero, pass to the tens function
            return tens(digits[1:])
        elif digits[1:] == [0,0]: # If a multiple of 100, just return 'thingy hundred'
            return '{} hundred'.format(units(digits[0]))
        else: # Otherwise, return 'thingy hundred and thingy'
            return '{} hundred and {}'.format(units(digits[0]),tens(digits[1:]))

    bigNames = ['thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion']
    digits = digitsOf(N)
    length = len(digits)
    for dummy in range(40-length): # Add leading zeroes until the number is 40 digits long
        digits.insert(0,0)
    string = hundreds(digits[-3:]) # Start by adding the words for the hundreds digits
    # Add thousands words
    if digits[-6:-3] == [0,0,0]:
        pass
    elif digits[-3:] == [0 for dummy in range(6 - 3)]:
        string = '{} thousand'.format(hundreds(digits[-6:-3]))
    elif digits[-3] == 0:
        string = '{} thousand and {}'.format(hundreds(digits[-6:-3]),string)
    else:
        string = '{} thousand, {}'.format(hundreds(digits[-6:-3]),string)

    # Add millions words
    if digits[-9:-6] == [0,0,0]:
        pass
    elif digits[-6:] == [0 for dummy in range(9 - 3)]:
        string = '{} million'.format(hundreds(digits[-9:-6]))
    elif digits[-6:-2] == [0 for dummy in range(9 - 3 - 2)]:
        string = '{} million and {}'.format(hundreds(digits[-9:-6]),string)
    else:
        string = '{} million, {}'.format(hundreds(digits[-9:-6]),string)

    # Add billions words
    if digits[-12:-9] == [0,0,0]:
        pass
    elif digits[-9:] == [0 for dummy in range(12 - 3)]:
        string = '{} billion'.format(hundreds(digits[-12:-9]))
    elif digits[-9:-2] == [0 for dummy in range(12 - 3 - 2)]:
        string = '{} billion and {}'.format(hundreds(digits[-12:-9]),string)
    else:
        string = '{} billion, {}'.format(hundreds(digits[-12:-9]),string)

    return string

print(inWords(596133237))
