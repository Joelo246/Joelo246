x = str(input("Please enter a word: "))
dictionary = {}
for character in x:
    if character in dictionary:
        dictionary[character] += 1
    else:
        dictionary[character] = 1
print("Given word:", x)
print("Count of each letter is:")

for character, count in dictionary.items() :
    print(character,"->",count)

print("total letters:")

CharacterTotal = 0

for character in x:
    if character:
        CharacterTotal = CharacterTotal+1

print(CharacterTotal)
