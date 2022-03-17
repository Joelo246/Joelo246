Sub_Data_8 = ("Sub_Data_8.txt")
Sub_String = ""
Sub_String2 = ""
Test = ""
Test2 = ""
Test3 = ""
Sub_String_Input = []
Sub_String_Output = []
ZeroSixNineArray = []
ZeroNineArray = []
TwoThreeFiveArray = []
ItemCount = 0
ArrayCount = 0
OneString = ""
SevenString = ""
FourString = ""
EightString = ""
SixString = ""
ZeroString = ""
NineString = ""
FiveString = ""
TwoString = ""
ThreeString = ""
PosOne = ""
PosTwo = ""
PosThree = ""
PosFour = ""
PosFive = ""
PosSix = ""
PosSeven = ""
TestString = ""
AnswerOne = ""
AnswerTwo = ""
AnswerThree = ""
AnswerFour = ""
Answers = ""
FinalAnswerArray = []

odds = range(1, 500, 2)
evens = range(2, 500, 2)

#for x in evens: #checking that ranges work
#    print(x)
#print(evens)

with open(Sub_Data_8) as data_file: #Opens input file and appends it to a string
    for x in data_file:
        Sub_String += x

for line in Sub_String: #open files and clean them of weird characters, adding consistent comma between every number
    Sub_String = Sub_String.replace("| ", "")
    Sub_String = Sub_String.replace("\n", " ") 

temp = Sub_String.split("|") #splits and extracts the letters from the string into an array
for x in temp:
    Sub_String2 += x

temp = Sub_String.split(" ") #splits and extracts the letters from the string into an array
for x in temp:   
    ItemCount = ItemCount+1
    if ItemCount > 0 and ItemCount < 11:
        Sub_String_Input.append(x)
    if ItemCount >= 11 and ItemCount <= 13:
        Sub_String_Output.append(x)
    if ItemCount == 14:
        Sub_String_Output.append(x)
        ItemCount = 0

ItemCount = 0
for x in Sub_String_Input: #this will attempt to extract the code sequence of each line
    ItemCount = ItemCount+1
    if len(x) == 2:
        OneString = x
    if len(x) == 3:
        SevenString = x
    if len(x) == 4:
        FourString = x
    if len(x) == 7:
        EightString = x
    if len(x) == 6:
        ZeroSixNineArray.append(x)
    if len(x) == 5:
        TwoThreeFiveArray.append(x)
    if ItemCount == 10: #First section takes the 10 code items, this section will attempt to determine each one's value
        ArrayCount = 0
        for y in SevenString:
            if y not in OneString:
                PosOne = y
        for y in ZeroSixNineArray: #this puts the three items from the ZeroSixNine array into three string variables
            ArrayCount = ArrayCount+1
            if ArrayCount == 1:
                Test = y
            if ArrayCount == 2:
                Test2 = y
            if ArrayCount == 3:
                Test3 = y
                ArrayCount = 0
                for x in OneString: #Use OneString to find Position 6 and 7
                    if x not in Test or x not in Test2 or x not in Test3:
                        PosSix = x
                    if x in Test and x in Test2 and x in Test3:
                        PosSeven = x
                if PosSix not in Test: #use posSix to find the SixString
                    SixString = Test
                    for x in FourString:
                        if x not in Test2 or x not in Test3:
                            PosTwo = x
                        else:
                            pass
                    if PosTwo not in Test2: #use SixString and PosTwo to find Zero and Nine
                        ZeroString = Test2
                        NineString = Test3
                    if PosTwo not in Test3:
                        ZeroString = Test3
                        NineString = Test2
                if PosSix not in Test2: #repeat for other possibilities
                    SixString = Test2
                    for x in FourString:
                        if x not in Test or x not in Test3:
                            PosTwo = x
                        else:
                            pass
                    if PosTwo not in Test:
                        ZeroString = Test
                        NineString = Test3
                    if PosTwo not in Test3:
                        ZeroString = Test3
                        NineString = Test
                if PosSix not in Test3: #repeat for other possibilities
                    SixString = Test3
                    for x in FourString:
                        if x not in Test or x not in Test3:
                            PosTwo = x
                        else:
                            pass
                    if PosTwo not in Test:
                        ZeroString = Test
                        NineString = Test2
                    if PosTwo not in Test2:
                        ZeroString = Test2
                        NineString = Test
                for x in FourString: #use Fourstring to find PosFour
                    if x not in PosSix and x not in PosSeven and x not in PosTwo:
                        PosFour = x
        for y in TwoThreeFiveArray: #with Zero Six Nine Discovered, break open TwoThreeFive Array into Strings
            ArrayCount = ArrayCount+1
            if ArrayCount == 1:
                Test = y
            if ArrayCount == 2:
                Test2 = y
            if ArrayCount == 3:
                Test3 = y
                ArrayCount = 0
                if PosSix not in Test: #use PosSix to find which is String Five
                    FiveString = Test
                    for x in EightString: #use EightString to find PosFive
                        if x not in FiveString and x not in PosSix:
                            PosFive = x
                    if PosFive not in Test2: #use pos5 to fine the three and two
                        ThreeString = Test2
                        TwoString = Test3
                    if PosFive not in Test3:
                        ThreeString = Test3
                        TwoString = Test2
                if PosSix not in Test2: #repeat for other possibilities
                    FiveString = Test2
                    for x in EightString:
                        if x not in FiveString and x not in PosSix:
                            PosFive = x
                    if PosFive not in Test:
                        ThreeString = Test
                        TwoString = Test3
                    if PosFive not in Test3:
                        ThreeString = Test3
                        TwoString = Test
                if PosSix not in Test3: #repeat for other possibilities
                    FiveString = Test3
                    for x in EightString:
                        if x not in FiveString and x not in PosSix:
                            PosFive = x
                    if PosFive not in Test2:
                        ThreeString = Test2
                        TwoString = Test3
                    if PosFive not in Test3:
                        ThreeString = Test3
                        TwoString = Test2
        for x in EightString: #Use Eightstring to find the last variable PosThree
            if x not in PosOne and x not in PosTwo and x not in PosSix and x not in PosSeven and x not in PosFour and x not in PosFive:
                PosThree = x    
        for x in Sub_String_Output: #Go into our final items with our newfound information to determine their numbers and sum them
            ItemCount = ItemCount+1
            if ItemCount == 11:
                AnswerOne = x
                print("Answer one is:", len(AnswerOne))
                print(AnswerOne)
                if len(AnswerOne) == 2:
                    Answers += "1"
                if len(AnswerOne) == 4:
                    Answers += "4"
                if len(AnswerOne) == 3:
                    Answers += "7"
                if len(AnswerOne) == 7:
                    Answers += "8"
                if len(AnswerOne) == 5:
                    if PosSix not in AnswerOne and PosFive not in AnswerOne:
                        Answers += "5"
                    if PosFour not in AnswerOne and PosSeven not in AnswerOne:
                        Answers += "2"                  
                    if PosFour not in AnswerOne and PosFive not in AnswerOne:
                        Answers += "3"
                if len(AnswerOne) == 6:
                    if PosFive not in AnswerOne:
                        Answers += "9"
                    if PosSix not in AnswerOne:
                        Answers += "6"                  
                    if PosTwo not in AnswerOne:
                        Answers += "0"
            if ItemCount == 12:
                AnswerTwo = x
                print("Answer two is:", len(AnswerTwo))
                print(AnswerTwo)
                if len(AnswerTwo) == 2:
                    Answers += "1"
                if len(AnswerTwo) == 4:
                    Answers += "4"
                if len(AnswerTwo) == 3:
                    Answers += "7"
                if len(AnswerTwo) == 7:
                    Answers += "8"
                if len(AnswerTwo) == 5:
                    if PosSix not in AnswerTwo and PosFive not in AnswerTwo:
                        Answers += "5"
                    if PosFour not in AnswerTwo and PosSeven not in AnswerTwo:
                        Answers += "2"                  
                    if PosFour not in AnswerTwo and PosFive not in AnswerTwo:
                        Answers += "3"
                if len(AnswerTwo) == 6:
                    if PosFive not in AnswerTwo:
                        Answers += "9"
                    if PosSix not in AnswerTwo:
                        Answers += "6"                  
                    if PosTwo not in AnswerTwo:
                        Answers += "0"
            if ItemCount == 13:
                AnswerThree = x
                print("Answer three is:", len(AnswerThree))
                print(AnswerThree)
                if len(AnswerThree) == 2:
                    Answers += "1"
                if len(AnswerThree) == 4:
                    Answers += "4"
                if len(AnswerThree) == 3:
                    Answers += "7"
                if len(AnswerThree) == 7:
                    Answers += "8"
                if len(AnswerThree) == 5:
                    if PosSix not in AnswerThree and PosFive not in AnswerThree:
                        Answers += "5"
                    if PosFour not in AnswerThree and PosSeven not in AnswerThree:
                        Answers += "2"                  
                    if PosFour not in AnswerThree and PosFive not in AnswerThree:
                        Answers += "3"
                if len(AnswerThree) == 6:
                    if PosFive not in AnswerThree:
                        Answers += "9"
                    if PosSix not in AnswerThree:
                        Answers += "6"                  
                    if PosTwo not in AnswerThree:
                        Answers += "0"
            if ItemCount == 14:
                AnswerFour = x
                print("Answer four is:", len(AnswerFour))
                print(AnswerFour)
                if len(AnswerFour) == 2:
                    Answers += "1"
                if len(AnswerFour) == 4:
                    Answers += "4"
                if len(AnswerFour) == 3:
                    Answers += "7"
                if len(AnswerFour) == 7:
                    Answers += "8"
                if len(AnswerFour) == 5:
                    if PosSix not in AnswerFour and PosFive not in AnswerFour:
                        Answers += "5"
                    if PosFour not in AnswerFour and PosSeven not in AnswerFour:
                        Answers += "2"                  
                    if PosFour not in AnswerFour and PosFive not in AnswerFour:
                        Answers += "3"
                if len(AnswerFour) == 6:
                    if PosFive not in AnswerFour:
                        Answers += "9"
                    if PosSix not in AnswerFour:
                        Answers += "6"                  
                    if PosTwo not in AnswerFour:
                        Answers += "0"
                FinalAnswerArray.append(int(Answers))
                ItemCount = 0
                OneString = ""
                SevenString = ""
                FourString = ""
                EightString = ""
                SixString = ""
                ZeroString = ""
                NineString = ""
                FiveString = ""
                TwoString = ""
                ThreeString = ""
                PosOne = ""
                PosTwo = ""
                PosThree = ""
                PosFour = ""
                PosFive = ""
                PosSix = ""
                PosSeven = ""
                TestString = ""
                AnswerOne = ""
                AnswerTwo = ""
                AnswerThree = ""
                AnswerFour = ""
                Answers = ""



print("So how's this lookin?", Answers)
print("And our array?", FinalAnswerArray)
print(PosOne)
print(PosTwo)
print(PosThree)
print(PosFour)
print(PosFive)
print(PosSix)
print(PosSeven)

print("And strings..", OneString)
print(TwoString)
print(ThreeString)
print(FourString)
print(FiveString)
print(SixString)
print(SevenString)
print(EightString)
print(NineString)
print(ZeroString)
                

                

                





#Test = ["abcefg", "abcdfg", "abdefg"]
#Test2 = "fcbdg"
#Test3 += "0"
#print(Test3)

#if Test3 in Test2:
#    print("Hurrah, a match!")
#for x in Test:
#    if Test3 not in x:
#        print(x)
#    if x not in Test2:
#        TestString = x

#print(TestString)