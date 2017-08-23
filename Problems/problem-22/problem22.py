def alphabeticalValue(word): # Returns sum of letter positions in alphabet
    value = 0
    for letter in word:
        value += ord(letter) - 64
    return value

with open('names.txt') as f: # Put names into list
    names = f.read().strip().replace('"','').split(',')

names = sorted(names) # Sort alphabetically

scores = [0 for i in range(len(names))]
for i, name in enumerate(names):
    scores[i] = alphabeticalValue(name) * (i+1)

print(sum(scores))
