# D Falck. Run this file, the command line interface will ask you for a number to print.

import math

def digitsOf(N): # Separates N into a list of its digits
    N = abs(N) # Make positive
    length = math.floor(math.log10(N)) + 1 # How many digits
    separated = []
    separated.append(int(N % 10)) # We build the list in reverse order, starting with the units digit
    for i in range(1,length): # Every digit can be found from N modulo something and the previous digit
        new = int((N % 10**(i+1) - separated[i-1])/(10**i))
        separated.append(new)
    separated.reverse() # Finally, put the list in the right order
    return separated

def inWords(N): # Returns the English words for N
    digitNames = ['zero','one','two','three','four','five','six','seven','eight','nine']
    teenNames = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tensNames = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    bigNames = ['thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion']

    def hundreds(digits): # Deals with triplets of digits
        def units(digit): # Deals with single digits
            return digitNames[digit]

        def tens(digits): # Deals with pairs of digits
            if digits[0] == 0: # If there's a leading zero, pass to the units function
                return units(digits[1])
            elif digits[0] == 1: # If the number is in the teens
                return teenNames[digits[1]]
            else: # For any number higher than 19
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

    digits = digitsOf(N)
    length = len(digits)
    for dummy in range(40-length): # Add leading zeroes until the number is 40 digits long
        digits.insert(0,0)
    string = hundreds(digits[-3:]) # Start by adding the words for the hundreds digits
    for i in range(len(bigNames)+1): # Now recursively add the words for the thousands, millions, etc. digits
        if digits[-(6+3*i):-(3+3*i)] == [0,0,0]: # Don't append anything if the digits are zeroes
            pass
        elif digits[-(3+3*i):] == [0 for dummy in range((6+3*i) - 3)]: # If everything else is zeroes, make this the only thing in the string
            string = '{} {}'.format(hundreds(digits[-(6+3*i):-(3+3*i)]),bigNames[i])
        elif digits[-(3+3*i):-2] == [0 for dummy in range((6+3*i) - 3 - 2)]: # If no digits until the tens, add an 'and'
            string = '{} {} and {}'.format(hundreds(digits[-(6+3*i):-(3+3*i)]),bigNames[i],string)
        else: # Otherwise just add on these digits and a comma
            string = '{} {}, {}'.format(hundreds(digits[-(6+3*i):-(3+3*i)]),bigNames[i],string)

    if N < 0: # If negative
        string = 'negative {}'.format(string)

    return string

if __name__ == '__main__': # Only run this when executing this file itself
    continuing = True # Runs a basic command line interface
    while continuing:
        request = input('Enter the integer you want printed (or \'s\' to stop):  ')
        if request == 's':
            continuing = False
        else:
            print(inWords(int(request)))
