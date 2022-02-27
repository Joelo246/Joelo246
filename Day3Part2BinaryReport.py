LifeSupRat = 0
OxyGenRat = 0
C02ScrubRat = 0
BinaryData = "Sub_Data_3.txt"
BinaryArray = []
GammaCounter = 0
EpsilonCounter = 0
OxyGenArray = []
OxyGenKey = str("") # yup yup yup defining way too many variables cause i'm a rookie ass newb AGAIN
OxyGenAnswer = 0
C02ScrubArray = []
C02ScrubKey = str("")
C02ScrubAnswer = 0
temp_array = []
Dig1Count = 0
Dig0Count = 0


with open(BinaryData) as data_file: #This counts the opening 1s and 0s
    for line in data_file:
        if line.startswith("1"):
            Dig1Count = Dig1Count+1
        elif line.startswith("0"):
            Dig0Count = Dig0Count+1
print("FIRST Dig 1 Count", Dig1Count)
print("FIRST Dig 0 Count", Dig0Count)

if Dig1Count >= Dig0Count: #appends the lines to oxygen or c02 arrays depending on where they belong
    OxyGenKey += "1"
    C02ScrubKey += "0"
    with open(BinaryData) as data_file:
        for line in data_file:
            if line.startswith("1"):
                OxyGenArray.append(line)
                Dig1Count = 0
                Dig0Count = 0
            if line.startswith("0"):
                C02ScrubArray.append(line)
                Dig1Count = 0
                Dig0Count = 0

if Dig0Count > Dig1Count: #appends the lines to oxygen od c02 arrays depending on where they belong
    OxyGenKey += "0"
    C02ScrubKey += "1"
    with open(BinaryData) as data_file:
        for line in data_file:
            if line.startswith("0"):
                OxyGenArray.append(line)
                Dig1Count = 0
                Dig0Count = 0
            if line.startswith("1"):
                C02ScrubArray.append(line)
                Dig1Count = 0
                Dig0Count = 0

SecondDig = [w[1] for w in OxyGenArray] #runs new count on updated array
Dig1Count = SecondDig.count("1")
Dig0Count = SecondDig.count("0")
print("Second Dig 1 Count", Dig1Count)
print("Second Dig 0 Count", Dig0Count)

if Dig1Count >= Dig0Count:
    OxyGenKey += "1"
    for x in OxyGenArray:
        if x.startswith(OxyGenKey):
            temp_array.append(x)
            Dig1Count = 0
            Dig0Count = 0

if Dig0Count > Dig1Count:
    OxyGenKey += "0"
    for x in OxyGenArray:
        if x.startswith(OxyGenKey):
            temp_array.append(x)
            Dig1Count = 0
            Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()

ThirdDig = [w[2] for w in OxyGenArray] #runs new count on updated array
Dig1Count = ThirdDig.count("1")
Dig0Count = ThirdDig.count("0")

print("Third Dig 1 Count", Dig1Count)
print("Third Dig 0 Count", Dig0Count)

if Dig1Count >= Dig0Count:
    OxyGenKey += "1"
    for x in OxyGenArray:
        if x.startswith(OxyGenKey):
            temp_array.append(x)
            Dig1Count = 0
            Dig0Count = 0

if Dig0Count > Dig1Count:
    OxyGenKey += "0"
    for x in OxyGenArray:
        if x.startswith(OxyGenKey):
            temp_array.append(x)
            Dig1Count = 0
            Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)

if len(OxyGenArray) > 1:
    FourthDig = [w[3] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = FourthDig.count("1")
    Dig0Count = FourthDig.count("0")
    print("Fourth Dig 1 Count", Dig1Count)
    print("Fourth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()    
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)

if len(OxyGenArray) > 1:
    FifthDig = [w[4] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = FifthDig.count("1")
    Dig0Count = FifthDig.count("0")
    print("Fifth Dig 1 Count", Dig1Count)
    print("Fifth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()    
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)

if len(OxyGenArray) > 1:
    SixthDig = [w[5] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = SixthDig.count("1")
    Dig0Count = SixthDig.count("0")
    print("Sixth Dig 1 Count", Dig1Count)
    print("Sixth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    SeventhDig = [w[6] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = SeventhDig.count("1")
    Dig0Count = SeventhDig.count("0")
    print("Seventh Dig 1 Count", Dig1Count)
    print("Seventh Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    EighthDig = [w[7] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = EighthDig.count("1")
    Dig0Count = EighthDig.count("0")
    print("Eighth Dig 1 Count", Dig1Count)
    print("Eighth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    NinthDig = [w[8] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = NinthDig.count("1")
    Dig0Count = NinthDig.count("0")
    print("Ninth Dig 1 Count", Dig1Count)
    print("Ninth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    TenthDig = [w[9] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = TenthDig.count("1")
    Dig0Count = TenthDig.count("0")
    print("Tenth Dig 1 Count", Dig1Count)
    print("Tenth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    EleventhDig = [w[10] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = EleventhDig.count("1")
    Dig0Count = EleventhDig.count("0")
    print("Eleventh Dig 1 Count", Dig1Count)
    print("Eleventh Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
           if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    TwelthDig = [w[11] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = TwelthDig.count("1")
    Dig0Count = TwelthDig.count("0")
    print("Twelth Dig 1 Count", Dig1Count)
    print("Twelth Dig 0 Count", Dig0Count)
    if Dig1Count >= Dig0Count:
        OxyGenKey += "1"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0
    if Dig0Count > Dig1Count:
        OxyGenKey += "0"
        for x in OxyGenArray:
            if x.startswith(OxyGenKey):
                temp_array.append(x)
                Dig1Count = 0
                Dig0Count = 0

OxyGenArray.clear()
for x in temp_array:
    OxyGenArray.append(x)
temp_array.clear()
if len(OxyGenArray) == 1:
    print("OxyGen Answer is:", OxyGenArray)
    for x in OxyGenArray:
        OxyGenAnswer = x
    OxyGenArray.clear()
    print("Oxy Answer Work!", OxyGenAnswer)
if len(OxyGenArray) > 1:
    TwelthDig = [w[11] for w in OxyGenArray] #runs new count on updated array
    Dig1Count = TwelthDig.count("1")
    Dig0Count = TwelthDig.count("0")
    print("Twelth Dig 1 Count", Dig1Count)
    print("Twelth Dig 0 Count", Dig0Count)
    print("And for Funsies OxyGenKey is...:", OxyGenKey)

SecondDigC02 = [w[1] for w in C02ScrubArray]
Dig1CountC02 = SecondDigC02.count("1")
Dig0CountC02 = SecondDigC02.count("0")
print("Second Dig c02 1 Count", Dig1CountC02)
print("Second Dig c02 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

ThirdDig = [w[2] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = ThirdDig.count("1")
Dig0CountC02 = ThirdDig.count("0")

print("Third C02 Dig 1 Count", Dig1CountC02)
print("Third C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

FourthDig = [w[3] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = FourthDig.count("1")
Dig0CountC02 = FourthDig.count("0")

print("Fourth C02 Dig 1 Count", Dig1CountC02)
print("Fourth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

FifthDig = [w[4] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = FifthDig.count("1")
Dig0CountC02 = FifthDig.count("0")

print("Fifth C02 Dig 1 Count", Dig1CountC02)
print("Fifth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

SixthDig = [w[5] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = SixthDig.count("1")
Dig0CountC02 = SixthDig.count("0")

print("Sixth C02 Dig 1 Count", Dig1CountC02)
print("Sixth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

SeventhDig = [w[6] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = SeventhDig.count("1")
Dig0CountC02 = SeventhDig.count("0")

print("Seventh C02 Dig 1 Count", Dig1CountC02)
print("Seventh C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

EighthDig = [w[7] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = EighthDig.count("1")
Dig0CountC02 = EighthDig.count("0")

print("Eighth C02 Dig 1 Count", Dig1CountC02)
print("Eighth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

NinthDig = [w[8] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = NinthDig.count("1")
Dig0CountC02 = NinthDig.count("0")

print("Ninth C02 Dig 1 Count", Dig1CountC02)
print("Ninth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

TenthDig = [w[9] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = TenthDig.count("1")
Dig0CountC02 = TenthDig.count("0")

print("Tenth C02 Dig 1 Count", Dig1CountC02)
print("Tenth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

EleventhDig = [w[10] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = EleventhDig.count("1")
Dig0CountC02 = EleventhDig.count("0")

print("Eleventh C02 Dig 1 Count", Dig1CountC02)
print("Eleventh C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

TwelthDig = [w[11] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = TwelthDig.count("1")
Dig0CountC02 = TwelthDig.count("0")

print("Twelth C02 Dig 1 Count", Dig1CountC02)
print("Twelth C02 Dig 0 Count", Dig0CountC02)

if Dig1CountC02 >= Dig0CountC02:
    C02ScrubKey += "0"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

if Dig0CountC02 > Dig1CountC02:
    C02ScrubKey += "1"
    for x in C02ScrubArray:
        if x.startswith(C02ScrubKey):
            temp_array.append(x)
            Dig1Countc02 = 0
            Dig0Countc02 = 0

C02ScrubArray.clear()
for x in temp_array:
    C02ScrubArray.append(x)
temp_array.clear()
if len(C02ScrubArray) == 1:
    print("C02 Scrubber Rating Answer is:", C02ScrubArray)
    for x in C02ScrubArray:
        C02ScrubAnswer = x

TwelthDig = [w[11] for w in C02ScrubArray] #runs new count on updated array
Dig1CountC02 = TwelthDig.count("1")
Dig0CountC02 = TwelthDig.count("0")

print("Twelth C02 Dig 1 Count", Dig1CountC02)
print("Twelth C02 Dig 0 Count", Dig0CountC02)
print("And for Funsies the Key is...", C02ScrubKey)
print("Oxy Answer Work!", OxyGenAnswer)
print("C02 Answer Work!", C02ScrubAnswer)

DecOxy = int(OxyGenAnswer, 2) #this code should convert the binary to decimal
DecC02 = int(C02ScrubAnswer, 2)
print("Oxy In Decimal:", DecOxy)
print("C02 In Decimal:", DecC02)

FinalAnswer = DecOxy * DecC02
print("Final Answer!", FinalAnswer)

#print("Current Oxy Array", OxyGenArray)
#print("Current C02 Array", C02ScrubArray)

# OxyGenArray.clear() #cleans arrays to refill with smaller set
# C02ScrubArray.clear()

# if Dig1Count >= Dig0Count: #repeat with smaller set
#    if OxyGenKey == "0":
#        OxyGenKey += "1"
#        C02ScrubKey += "0"
#        with open(BinaryData) as data_file:
#            for line in data_file:
#                if line.startswith("01"):
#                    OxyGenArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#                if line.startswith("10"):
#                    C02ScrubArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#    elif OxyGenKey == "1":
#        OxyGenKey += "1"
#        C02ScrubKey += "0"
#        with open(BinaryData) as data_file:
#            for line in data_file:
#                if line.startswith("11"):
#                    OxyGenArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#                if line.startswith("00"):
#                    C02ScrubArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#
#if Dig0Count > Dig1Count:
#    if OxyGenKey == "0":
#        OxyGenKey += "0"
#        C02ScrubKey += "1"
#        with open(BinaryData) as data_file:
#            for line in data_file:
#                if line.startswith("00"):
#                    OxyGenArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#                if line.startswith("11"):
#                    C02ScrubArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#    elif OxyGenKey == "1":
#        OxyGenKey += "0"
#        C02ScrubKey += "1"
#        with open(BinaryData) as data_file:
#            for line in data_file:
#                if line.startswith("10"):
#                    OxyGenArray.append(line)
#                    Dig1Count = 0
#                    Dig0Count = 0
#               if line.startswith("01"):
#                   C02ScrubArray.append(line)
#                   Dig1Count = 0
#                   Dig0Count = 0
#
#ThirdDig = [w[2] for w in OxyGenArray] #runs new count on updated array
#Dig1Count = SecondDig.count("1")
#Dig0Count = SecondDig.count("0")
#
#if len(OxyGenArray) == 1:
#    print("Stop, the answer is!", OxyGenArray)
#if len(C02ScrubArray) == 1:
#    print("Stop, the answer is!", C02ScrubArray)
#
#print("Here's out Current Dig1 Count", Dig1Count)
#print("Here's out Current Dig2 Count", Dig0Count)
#print("Current Oxy Array", OxyGenArray)
#print("Current C02 Array", C02ScrubArray)    
#print("Current Oxy Key", OxyGenKey)
#print("Current C02 Key", C02ScrubKey)

#OxyGenArray.clear() #cleans arrays to refill with smaller set
#C02ScrubArray.clear()

#        Temp_Data1 += line[0]
#        Temp_Data2 += line[1]
#        Temp_Data3 += line[2]
#        Temp_Data4 += line[3]
#        Temp_Data5 += line[4]
#        Temp_Data6 += line[5]
#        Temp_Data7 += line[6]
#        Temp_Data8 += line[7]
#        Temp_Data9 += line[8]
#        Temp_Data10 += line[9]
#        Temp_Data11 += line[10]
#        Temp_Data12 += line[11]
#
# for x in Temp_Data1: #each of these blocks counts the 1s and 0s in each digit set and then appends a  
#    if x == "1":      #final 1 or 0 to the answer based on which there are more of
#        Dig1Count = Dig1Count+1
#    elif x == "0":
#        Dig0Count = Dig0Count+1
# if Dig1Count > Dig0Count:
#    with open(BinaryData) as data_file:
#        for line in data_file:
#            if line.startswith("1")
#
#    Dig1Count = 0
#    Dig0Count = 0
# if Dig0Count > Dig1Count:
#    FinalAnswer.append(0)
#    FinalAnswerString += "0"
#    ReverseAnswerString += "1"
#    Dig1Count = 0
#    Dig0Count = 0