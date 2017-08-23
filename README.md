# To do

___
- testPs
- Simplify `digitsOf()` function to use `str(N)` and then string indexing rather than modular arithmetic and lists.

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
