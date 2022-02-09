WordString = str(input("Give me some weird words!(no spaces!)"))
WordStringCheck = WordString.isalpha() #Checks if the string is alphabet characters only
while WordStringCheck == False: #If this check fails, forces user to reenter a new string
    WordString = str(input("I said no funny business, letters only!"))
    WordStringCheck = WordString.isalpha()
digit = int(input("Give me a number!"))

AltCharTotal = 0
CharacterTotal = 0

for character in WordString:
    if character:
        CharacterTotal = CharacterTotal+1 #counts the characters in the string

if digit > CharacterTotal: #checks to make sure number is valid
    digit = int(input("A number smaller or equal to your word(s) length please!"))

CASESWAP = WordString.swapcase() #reverses upper and lower cases

AltCharTotal = len(WordString) #alternate way to count chars
print("Your Character Total is: ", CharacterTotal)
print("And my altcount has...: ", AltCharTotal)
print("And digit #%d is...:" % digit, WordString[digit-1]) #finds and prints the corresponding letter
print("AND... here's your shit flipped and reversed:", "".join(reversed(CASESWAP)))


#
# if digit <= CharacterTotal:
#    YourLetter = digit in WordString
#    print("Your words have CharacterTotal letters in them and the digit letter is %" %YourLetter)
