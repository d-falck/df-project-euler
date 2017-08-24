# Project Euler problem solutions
#### D Falck

Hi! These are all my solutions to the [Project Euler](https://projecteuler.net/archives) problems.

*Please don't look at the solution to a problem until you've at least solved it for yourself once!*

They're all coded in Python 3.6. Information about my setup as well as full explanations and writeups are available [at my website](http://dfalck.xyz).

## To do

___
- *Done in problem 32* Simplify `digitsOf()` function to use `str(N)` and then string indexing rather than modular arithmetic and lists.

 *Currently looks like:*

```python
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
```
