values = [200,100,50,20,10,5,2,1]
toMake = 200

possibleCombinations = []
currentCombination = [] # (an empty stack, holds the current combination of coins in descending value)
currentTotal = 0

def depthFirstSearch(startFrom): # This calls itself recursively
    global currentTotal
    # ITERATE
    for value in values[startFrom:]:
        if value <= toMake - currentTotal:
            currentCombination.append(value)
            currentTotal += value
            depthFirstSearch(values.index(value))
    # UPDATE
    if sum(currentCombination) == toMake:
        possibleCombinations.append(currentCombination[:])
    # TERMINATE
    if currentCombination == []: # We've got to the very end of the whole recursive thing
        return
    else: # Return to the parent instance
        currentTotal += - currentCombination.pop()
        return

depthFirstSearch(0) # call the whole thing

    # startFrom = values.index(currentCombination.pop()) + 1 # Reached the end of possibilities here, pop the last value off and carry on from the last branch
print(len(possibleCombinations))
