from ast import Sub

Sub_Data_6 = ("Sub_Data_6.txt")
Sub_String = ""
Sub_Array = []
Final_Array = []
Final_Array2 = []
Final_Array3 = []
Final_Array4 = []
Final_Array5 = []
Final_Array6 = []
Final_Array7 = []
Final_Array8 = []
Final_Array9 = []
Final_Array10 = []
Sub_Array_Temp = []
FinalString = ""
tm = ""
DayCounter = 0
ArrayCounter = 0
FinalTotal = 0
ZeroCount = 0
OneCount = 0
TwoCount = 0
ThreeCount = 0
FourCount = 0
FiveCount = 0
SixCount = 0
SevenCount = 0
EightCount = 0
ZeroTemp = 0
OneTemp = 0
TwoTemp = 0
ThreeTemp = 0
FourTemp = 0
FiveTemp = 0
SixTemp = 0
SevenTemp = 0
EightTemp = 0

f = ("Sub_Array_Data.txt")
final = ("Final_Sub.txt")

with open(Sub_Data_6) as data_file: #Opens input file and appends it to a string
    for x in data_file:
        Sub_String += x

temp = Sub_String.split(",") #splits and extracts the integers from the string into an array
for x in temp:
    xz = (int(x))
    Sub_Array.append(xz)
    ArrayCounter = ArrayCounter+1

#print(Sub_Array)
#print(len(Sub_Array))

for each in Sub_Array:
    y = each
    if y == 1:
        OneCount = OneCount+1
    if y == 2:
        TwoCount = TwoCount+1
    if y == 3:
        ThreeCount = ThreeCount+1
    if y == 4:
        FourCount = FourCount+1
    if y == 5:
        FiveCount = FiveCount+1
    if y > 5:
        EightCount = EightCount+1
        Final_Array.append(y)

#print(OneCount)
#print(TwoCount)
#print(ThreeCount)
#print(FourCount)
#print(FiveCount)
#print(EightCount)
#print(Final_Array)

DayCounter = 0

while DayCounter <= 255:  
    DayCounter = DayCounter+1           
    ZeroTemp = ZeroCount
    OneTemp = OneCount
    TwoTemp = TwoCount
    ThreeTemp = ThreeCount
    FourTemp = FourCount
    FiveTemp = FiveCount
    SixTemp = SixCount
    SevenTemp = SevenCount
    EightTemp = EightCount
    ZeroCount = 0
    OneCount = 0
    TwoCount = 0
    ThreeCount = 0
    FourCount = 0
    FiveCount = 0
    SixCount = 0
    SevenCount = 0
    EightCount = 0
    EightCount = ZeroTemp
    SevenCount = EightTemp
    SixCount = SevenTemp + ZeroTemp
    FiveCount = SixTemp
    FourCount = FiveTemp
    ThreeCount = FourTemp
    TwoCount = ThreeTemp
    OneCount = TwoTemp
    ZeroCount = OneTemp

print(ZeroCount)
print(OneCount)
print(TwoCount)
print(ThreeCount)
print(FourCount)
print(FiveCount)
print(SixCount)
print(SevenCount)
print(EightCount)

FinalTotal = EightCount + SevenCount + SixCount + FiveCount + FourCount + ThreeCount + TwoCount + OneCount + ZeroCount
        
print(FinalTotal)

#for z in Sub_Array_Temp:
#        FinalString += ' ' + z
#        print("what's happen with these day counts", DayCounter)
#        for i in Sub_Array_Temp:
#            print("what's happen with these sub_arrays", Sub_Array)
#                Sub_Array_Temp.append(int(6))
#                Sub_Array_Temp.append(int(8))
#                Sub_Array_Temp.append(int(xz-1))
#                print("what's happen with these sub_arrays", Sub_Array_Temp)
#    Sub_Array_Temp.clear()
#    Sub_Array.clear()
#        Sub_Array.clear()  
#        Sub_Array_Temp.clear()
#    print("what's happen with these xz's", xz) # just trying to look under the hood here and find the errors
#    final = open("Final_Sub.txt", "a") #attempting to learn how to move this stuff into text files, didn't quite work
#    if ArrayCounter > 1:
#        with open(f) as temp:
#            for x in temp:
#                tm += x
#            xy = tm.split("\n")
#            for u in xy:
#                final.write(u + "\n")
#    open("Sub_Array_Temp.txt", 'w').close()
#   print("what's happen with these Arraycounts", ArrayCounter)
#    if ArrayCounter >= 1: #and ArrayCounter <= 29:
#         for z in Sub_Array_Temp:
#            FinalString += ' ' + str(z)
#    if ArrayCounter >= 30 and ArrayCounter <= 59:
#         for z in Sub_Array_Temp:
#            Final_Array2.append(z)
#    if ArrayCounter >= 60 and ArrayCounter <= 89:
#         for z in Sub_Array_Temp:
#            Final_Array3.append(z)
#    if ArrayCounter >= 90 and ArrayCounter <= 129:
#         for z in Sub_Array_Temp:
#            Final_Array4.append(z)
#    if ArrayCounter >= 130 and ArrayCounter <= 159:
#         for z in Sub_Array_Temp:
#            Final_Array5.append(z)
#    if ArrayCounter >= 160 and ArrayCounter <= 199:
#         for z in Sub_Array_Temp:
#            Final_Array6.append(z)
#    if ArrayCounter >= 200 and ArrayCounter <= 229:
#         for z in Sub_Array_Temp:
#            Final_Array7.append(z)
#    if ArrayCounter >= 230 and ArrayCounter <= 259:
#         for z in Sub_Array_Temp:
#            Final_Array8.append(z)
#    if ArrayCounter >= 260 and ArrayCounter <= 299:
#         for z in Sub_Array_Temp:
#            Final_Array9.append(z)
#    elif ArrayCounter > 299:
#         for z in Sub_Array_Temp:
#            Final_Array10.append(z)
#        print("what's happen with these final arrays", Final_Array)

#            with open(f) as temp:
#                for x in temp:
#                    tm += x
#            xy = tm.split("\n")
#            for u in xy:
#                ud = int(u)
#                Sub_Array.append(ud)
#            open("Sub_Array_Temp.txt", 'w').close()
#            for y in Sub_Array:
#                if y == 0:
#                    f = open("Sub_Array_Temp.txt", "a")
#                    f.write("6" + "\n")
#                    f.write("8" + "\n")
#                    Sub_Array_Temp.append(int(6))
#                    Sub_Array_Temp.append(int(8))
#                    print("what's happen with these sub_arrays temps", Sub_Array_Temp)
#                elif y != 0:
#                    f = open("Sub_Array_Temp.txt", "a")
#                    item = int(y-1)
#                    f.write(item + "\n")
#                    Sub_Array_Temp.append(int(y-1))



#print(len(Sub_Array))
#print(len(Final_Array))

#    if ArrayCounter >=1 and ArrayCounter <=74:
#        Sub_Array.append(int(x))
#    if ArrayCounter >=75 and ArrayCounter <=149:
#        Sub_Array2.append(int(x))
#    if ArrayCounter >=150 and ArrayCounter <=224:
#        Sub_Array3.append(int(x))
#    if ArrayCounter >=225 and ArrayCounter <=300:
#        Sub_Array4.append(int(x))

#while DayCounter <= 256: #main program, attempts to run an 80 day expanding counter of the fish births
#    if DayCounter >=1:
#        Sub_Array.clear()
#        Sub_Array2.clear()
#        Sub_Array3.clear()
#        Sub_Array4.clear()
#        for i in Sub_Array_Temp:
#            Sub_Array.append(i)
#        for i in Sub_Array_Temp2:
#            Sub_Array2.append(i)
#        for i in Sub_Array_Temp3:
#            Sub_Array3.append(i)
#        for i in Sub_Array_Temp4:
#            Sub_Array4.append(i)
#    Sub_Array_Temp.clear()
#    Sub_Array_Temp2.clear()
#    Sub_Array_Temp3.clear()
#    Sub_Array_Temp4.clear()
#    DayCounter = DayCounter+1
#    for x in Sub_Array:
#        if x == 0:
#            Sub_Array_Temp.append(6)
#            Sub_Array_Temp.append(8)
#        else:            
#            Sub_Array_Temp.append(x-1)
#    for x in Sub_Array2:
#        if x == 0:
#            Sub_Array_Temp2.append(6)
#            Sub_Array_Temp2.append(8)
#        else:            
#            Sub_Array_Temp2.append(x-1)
#    for x in Sub_Array3:
#        if x == 0:
#            Sub_Array_Temp3.append(6)
#            Sub_Array_Temp3.append(8)
#        else:            
#            Sub_Array_Temp3.append(x-1)
#    for x in Sub_Array4:
#        if x == 0:
#            Sub_Array_Temp4.append(6)
#            Sub_Array_Temp4.append(8)
#        else:            
#            Sub_Array_Temp4.append(x-1)

