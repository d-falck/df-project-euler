values = [200,100,50,20,10,5,2,1]
toMake = 200

possibleCombinations = []
currentCombination = [] # An empty stack, holds the current combination of coins in descending value

def depthFirstSearch(startFrom): # This calls itself recursively
    global currentTotal
    # ITERATE
    for value in values[startFrom:]:
        if value <= toMake -  sum(currentCombination):
            currentCombination.append(value)
            depthFirstSearch(values.index(value))
    # UPDATE
    if sum(currentCombination) == toMake:
        possibleCombinations.append(currentCombination[:])
    # TERMINATE
    if currentCombination == []: # We've got to the very end of the whole recursive thing
        return
    else: # Return to the parent instance
        currentCombination.pop()
        return

depthFirstSearch(0) # Call the whole thing
print(len(possibleCombinations))
