import math
from numberprinter import *

letterSum = 0
for i in range(1,1001):
    string = inWords(i)
    letterSum += len(string.replace('-','').replace(' ',''))
print(letterSum)
