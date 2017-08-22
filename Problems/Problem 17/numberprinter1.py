import math

def digits(N):
    length = math.floor(math.log10(N)) + 1 # How many digits
    separated = []
    separated.append(int(N % 10))
    for i in range(1,length):
        new = int((N % 10**(i+1) - separated[i-1])/(10**i))
        separated.append(new)
    separated.reverse()
    return separated

def wordyDigit(digit): # Generates the English word for the single digit 'digit'
    if digit == 0:
        return 'zero'
    elif digit == 1:
        return 'one'
    elif digit == 2:
        return 'two'
    elif digit == 3:
        return 'three'
    elif digit == 4:
        return 'four'
    elif digit == 5:
        return 'five'
    elif digit == 6:
        return 'six'
    elif digit == 7:
        return 'seven'
    elif digit == 8:
        return 'eight'
    elif digit == 9:
        return 'nine'

def wordyTens(twoDigits): # Generates the English word for the two digits 'twoDigits'
    if twoDigits[0] == 0:
        return wordyDigit(twoDigits[1])
    elif twoDigits[0] == 1:
        if twoDigits[1] == 0:
            return 'ten'
        elif twoDigits[1] == 1:
            return 'eleven'
        elif twoDigits[1] == 2:
            return 'twelve'
        elif twoDigits[1] == 3:
            return 'thirteen'
        elif twoDigits[1] == 4:
            return 'fourteen'
        elif twoDigits[1] == 5:
            return 'fifteen'
        elif twoDigits[1] == 6:
            return 'sixteen'
        elif twoDigits[1] == 7:
            return 'seventeen'
        elif twoDigits[1] == 8:
            return 'eighteen'
        elif twoDigits[1] == 9:
            return 'nineteen'
    elif twoDigits[0] == 2: # Find name for the tens digit
        firstWord = 'twenty'
    elif twoDigits[0] == 3:
        firstWord = 'thirty'
    elif twoDigits[0] == 4:
        firstWord = 'forty'
    elif twoDigits[0] == 5:
        firstWord = 'fifty'
    elif twoDigits[0] == 6:
        firstWord = 'sixty'
    elif twoDigits[0] == 7:
        firstWord = 'seventy'
    elif twoDigits[0] == 8:
        firstWord = 'eighty'
    elif twoDigits[0] == 9:
        firstWord = 'ninety'

    if twoDigits[1] == 0: # Now concatenate the tens digit with the units digit
        return firstWord
    else:
        return '{}-{}'.format(firstWord,wordyDigit(twoDigits[1]))

def wordyHundreds(threeDigits): # Generates the English word for the three digits 'threeDigits'
    if threeDigits[0] == 0:
        return wordyTens(threeDigits[1:])
    elif threeDigits[1:] == [0,0]:
        return '{} hundred'.format(wordyDigit(threeDigits[0]))
    else:
        return '{} hundred and {}'.format(wordyDigit(threeDigits[0]),wordyTens(threeDigits[1:]))

def wordyThousands(sixDigits): # Generates the English word for the six digits 'sixDigits'
    if sixDigits[0:3] == [0,0,0]:
        return wordyHundreds(sixDigits[3:])
    elif sixDigits[3:] == [0 for dummy in range(6 - 3)]:
        return '{} thousand'.format(wordyHundreds(sixDigits[0:3]))
    elif sixDigits[3] == 0:
        return '{} thousand and {}'.format(wordyHundreds(sixDigits[0:3]),wordyHundreds(sixDigits[3:]))
    else:
        return '{} thousand {}'.format(wordyHundreds(sixDigits[0:3]),wordyHundreds(sixDigits[3:]))

def wordyMillions(nineDigits): # Generates the English word for the nine digits 'nineDigits'
    if nineDigits[0:3] == [0,0,0]:
        return wordyThousands(nineDigits[3:])
    elif nineDigits[3:] == [0 for dummy in range(9 - 3)]:
        return '{} million'.format(wordyHundreds(nineDigits[0:3]))
    elif nineDigits[3:-1] == [0 for dummy in range(9 - 3 - 2)]:
        return '{} million and {}'.format(wordyHundreds(nineDigits[0:3]),wordyThousands(nineDigits[3:]))
    else:
        return '{} million {}'.format(wordyHundreds(nineDigits[0:3]),wordyThousands(nineDigits[3:]))

def wordyBillions(twelveDigits): # Generates the English word for the twelve digits 'twelveDigits'
    if twelveDigits[0:3] == [0,0,0]:
        return wordyMillions(twelveDigits[3:])
    elif twelveDigits[3:] == [0 for dummy in range(12 - 3)]:
        return '{} billion'.format(wordyHundreds(twelveDigits[0:3]))
    elif twelveDigits[3:-1] == [0 for dummy in range(12 - 3 - 2)]:
        return '{} billion and {}'.format(wordyHundreds(twelveDigits[0:3]),wordyMillions(twelveDigits[3:]))
    else:
        return '{} billion {}'.format(wordyHundreds(twelveDigits[0:3]),wordyMillions(twelveDigits[3:]))

def wordyNumber(N): # Returns the English words for the number N below a trillion, without commas
    number = digits(N)
    if number == [4,2]:
        return 'life, the universe and everything'
    else:
        while len(number) < 12:
            number.insert(0,0)
        return wordyBillions(number)



while True:
    request = input('Type in the number you want printed (or input \'s\' to stop):')
    if request == 's':
        break
    else:
        print(wordyNumber(int(request)))
