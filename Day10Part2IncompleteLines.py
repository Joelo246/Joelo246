Sub_Data_10 = ("Sub_Data_10.txt")
SD10String = ""
Temp = ""
OpenArray = []
CloseArray = []
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
TempString = ""
FinalString = ""
StupidityCount = 0
ScoresArray = []
LineCompleter = []
Triggercount = 0
LineNo = 0
CorruptLines = []

def DelLast(s):
    return s[s.rfind('\n')]

with open(Sub_Data_10) as data_file:
    for line in data_file:
        SD10String += line

Temp = SD10String.split("\n")
print("and temp?", len(Temp))
for x in Temp:
    LineNo = LineNo+1
    if CorruptionCounter > 0:
        Triggercount = Triggercount+1
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
                CorruptLines.append(LineNo)

#print(CorruptionHits)
#print(NewString)
#print(len(NewString))
#print(len(Temp))
#print(len(SD10String))
#print(CorruptionHits)

#for x in CorruptionHits:
#    if x == ")":
#        FinalAnswer = FinalAnswer+3
#    if x == "]":
#        FinalAnswer = FinalAnswer+57
#    if x == "}":
#        FinalAnswer = FinalAnswer+1197
#    if x == ">":
#        FinalAnswer = FinalAnswer+25137

#print("Final Answer is...", FinalAnswer)

#And heading onto part two here:

OpenArray = []
print("Triggercount?", Triggercount)
print(CorruptionHits)
print(len(CorruptionHits))
print(CorruptLines)
print("Errorcheckerextraordinaire, how's my new stirng?", NewString)
#for x in NewString:
#    print(x)

LineNo = 0
Temp = SD10String.split("\n")
for x in Temp:
    if LineNo == 0:
        FinalString += x
    LineNo = LineNo+1
    for item in OpenArray[::-1]:
        if item == "(":
            TempString += ")"
            LineCompleter.append(")")
        if item == "[":
            TempString += "]"
            LineCompleter.append("]")
        if item == "{":
            TempString += "}"
            LineCompleter.append("}")
        if item == "<":
            TempString += ">"
            LineCompleter.append(">")
    if LineNo > 1:
        FinalString += TempString + "\n"
    if LineNo > 1 and LineNo not in CorruptLines:
        FinalString += x
    FinalAnswer = 0
    for item in LineCompleter:
        FinalAnswer = FinalAnswer * 5
        if item == ")":
            FinalAnswer = FinalAnswer+1
        if item == "]":
            FinalAnswer = FinalAnswer+2
        if item == "}":
            FinalAnswer = FinalAnswer+3
        if item == ">":
            FinalAnswer = FinalAnswer+4
    if FinalAnswer != 0:
        ScoresArray.append(FinalAnswer)
    TempString = ""
    LineCompleter = []
    OpenArray = []
    if LineNo in CorruptLines:
        continue
    if LineNo not in CorruptLines:
        for y in x:
            if y in OpenBracks:
                OpenArray.append(y)
            if y in CloseBracks:
                if OpenArray[-1] + y == Pair1 or OpenArray[-1] + y == Pair2 or OpenArray[-1] + y == Pair3 or OpenArray[-1] + y == Pair4:
                    OpenArray.pop()

for item in OpenArray[::-1]:
    if item == "(":
        TempString += ")"
        LineCompleter.append(")")
    if item == "[":
        TempString += "]"
        LineCompleter.append("]")
    if item == "{":
        TempString += "}"
        LineCompleter.append("}")
    if item == "<":
        TempString += ">"
        LineCompleter.append(">")
FinalString += TempString + "\n"
FinalAnswer = 0
for item in LineCompleter:
    FinalAnswer = FinalAnswer * 5
    if item == ")":
        FinalAnswer = FinalAnswer+1
    if item == "]":
        FinalAnswer = FinalAnswer+2
    if item == "}":
        FinalAnswer = FinalAnswer+3
    if item == ">":
        FinalAnswer = FinalAnswer+4

if FinalAnswer != 0:
    ScoresArray.append(FinalAnswer)
    TempString = ""
    LineCompleter = []
    OpenArray = []


print("How we doin?", ScoresArray)
print(len(ScoresArray))

ScoresArray.sort()
print(ScoresArray[26])
print("How we doin?", ScoresArray)