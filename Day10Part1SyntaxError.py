Sub_Data_10 = ("Sub_Data_10.txt")
SD10String = ""
Temp = ""
OpenArray = []
OpenBracks = ["[", "(", "{", "<"]
CloseBracks = ["]", ")", "}", ">"]
Pair1 = "[]"
Pair2 = "()"
Pair3 = "{}"
Pair4 = "<>"
CorruptionCounter = 0
CorruptionHits = []
NewString = ""
FinalAnswer = 0

def DelLast(s):
    return s[s.rfind('\n')]

with open(Sub_Data_10) as data_file:
    for line in data_file:
        SD10String += line

Temp = SD10String.split("\n")
for x in Temp:
    if CorruptionCounter > 0:
        NewString = DelLast(NewString)
    CorruptionCounter = 0
    NewString += x + "\n"
    OpenArray = []
    for y in x:
        if CorruptionCounter > 0:
            break
        if y in OpenBracks:
            OpenArray.append(y)
        if y in CloseBracks:
            if OpenArray[-1] + y == Pair1 or OpenArray[-1] + y == Pair2 or OpenArray[-1] + y == Pair3 or OpenArray[-1] + y == Pair4:
                OpenArray.pop()
            elif OpenArray[-1] + y != Pair1 and OpenArray[-1] + y != Pair2 and OpenArray[-1] + y != Pair3 and OpenArray[-1] + y != Pair4:
                CorruptionCounter = CorruptionCounter+1
                CorruptionHits.append(y)

#print(CorruptionHits)
#print(NewString)
print(len(NewString))
print(len(Temp))
print(len(SD10String))
print(CorruptionHits)

for x in CorruptionHits:
    if x == ")":
        FinalAnswer = FinalAnswer+3
    if x == "]":
        FinalAnswer = FinalAnswer+57
    if x == "}":
        FinalAnswer = FinalAnswer+1197
    if x == ">":
        FinalAnswer = FinalAnswer+25137

print("Final Answer is...", FinalAnswer)
