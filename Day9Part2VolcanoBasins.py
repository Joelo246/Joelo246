Sub_Data = ("Sub_Data_9.txt")
Sub_Data_Array = ""
SubDataArray = []
NumCount = 0
DangerArray = []
FinalAnswer = 0
NumCountArray = []
BasinArray = []
TempBasin = 0
NumRay = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


with open(Sub_Data) as Data_File:
    for line in Data_File:
        Sub_Data_Array += line

#for line in Sub_Data_Array:
#    QuickCount = QuickCount+1
#    if QuickCount < 105:
#        pass

#print(LineString[99])
#if Sub_Data_Array[0] > Sub_Data_Array[-1]:
#    print(Sub_Data_Array[0])


#for x in Sub_Data_String: #open files and clean them of weird characters, adding consistent comma between every number
#    Sub_Data_String = Sub_Data_String.replace("\n", "")


#for x in Sub_Data_String:
#    Sub_DataArray.append(int(x))

BabyS = 1
BabyBackS = -1
BigBackS = -101
BigS = 101
PosArray = []
DoubleCheckArray = []
CheckedArray = []
NoHitter = 0
FinalScoreArray = []

NumCount = -1
for x in Sub_Data_Array:
    NumCount = NumCount+1
    if x in NumRay and NumCount not in DoubleCheckArray: #added last line to try to avoid double counting basins
        TempBasin = TempBasin+1
        PosArray.append(NumCount)
        while len(PosArray) > 0: #the idea here is to create a recursive loop where the computer keeps checking each uNumCounthecked item until it finda all the items.
#            NoHitter = 0 #This is to track when it stops finding any new items - obsoleted, i just check that CheckArray matches PosArray
            for y in PosArray:
                if y not in CheckedArray:
                    CheckedArray.append(y)
                    if (y+BabyS) <= 10000:
                        if Sub_Data_Array[y+BabyS] in NumRay and (y+BabyS) not in PosArray: #checks one index right
                            TempBasin = TempBasin+1 #one point for our basin size counter
#                            NoHitter = NoHitter+1
                            PosArray.append(y+BabyS) #add the coordinate so we don't double count
                    if (y+BigS) <= 10000:
                        if Sub_Data_Array[y+BigS] in NumRay and (y+BigS) not in PosArray: #checks one index down
                            TempBasin = TempBasin+1
#                            NoHitter = NoHitter+1
                            PosArray.append(y+BigS)
                    if (y+BabyBackS) >= 0:
                        if Sub_Data_Array[y+BabyBackS] in NumRay and (y+BabyBackS) not in PosArray: #checks one index left
                            TempBasin = TempBasin+1
#                            NoHitter = NoHitter+1
                            PosArray.append(y+BabyBackS)
                    if (y+BigBackS) >= 0:
                        if Sub_Data_Array[y+BigBackS] in NumRay and (y+BigBackS) not in PosArray: #checks one index up
                            TempBasin = TempBasin+1
#                            NoHitter = NoHitter+1
                            PosArray.append(y+BigBackS)
            if PosArray == CheckedArray:
                    FinalScoreArray.append(TempBasin)
#                    if TempBasin > 108:
#                        print("Okay wtf basin?", CheckedArray)
#                        print("size?", len(CheckedArray))
#                        print(TempBasin)
#                        for x in CheckedArray:
#                            print(Sub_Data_Array[x])
                    for x in PosArray:
                        DoubleCheckArray.append(x) #make it so we don't keep going into same basins
                    CheckedArray = [] #reset variables for next basin
                    PosArray = []
                    TempBasin = 0

print("Final Score Array...", FinalScoreArray)
FinalScoreArray.sort()
FinalScoreArray.reverse()
print("Final Score Array...", FinalScoreArray)
print(FinalScoreArray[0:4])
FinalAnswer = FinalScoreArray[0] * FinalScoreArray[1] * FinalScoreArray[2]
print(FinalAnswer)
                


#        while x[NC+BabyS] in NumRay:
#            TempBasin = TempBasin+1
#            PosArray.append[NC+BabyS]
#            while x[NC+BabyS+BigS] in NumRay:
#                TempBasin = TempBasin+1
#                PosArray.append[NC+BabyS+BigS]
#                BigS = BigS + 101
#            while x[NC+BigBackS] in NumRay:
#                TempBasin = TempBasin+1
#                BigBackS = BigBackS - 101
#            BigBackS = -101
#            BigS = 101
#            BabyS = BabyS+1
#        BabyS = 1
#        while x[NC+BigS] in NumRay:
#            TempBasin = TempBasin+1
#            while x[NC+BigS+BigS] in NumRay:
#                TempBasin = TempBasin+1
#                BigS = BigS + 101
#            while x[NC+BigBackS] in NumRay:
#                TempBasin = TempBasin+1
#                BigBackS = BigBackS - 101
#            BigBackS = -101
#            BigS = 101
#            BabyS = BabyS+1
#        BabyS = 1


        #print(x)
#    NC = NC+1
#    if NC == 0:
#        if x < Sub_Data_Array[NC+BabyS] and x < Sub_Data_Array[NC+BigS]:
#            TempBasin = TempBasin+3
#            if Sub_Data_Array[NC+BabyS] < Sub_Data_Array[NC+BabyS+1]:
#                TempBasin = TempBasin+1
#                BabyS = BabyS+1
#            BabyS = 1
            

#    if NumCount > 0 and NumCount < 99:
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount+100]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)
#    if NumCount == 99:
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+100]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)
#    if NumCount in range(100, 9801, 100):
#        if x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount+100] and x < Sub_Data_Array[NumCount-100]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)
#    if NumCount in range (199, 9901, 100):
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+100] and x < Sub_Data_Array[NumCount-100]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)
#    if NumCount > 9900 and NumCount < 9999:
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount-100] and x < Sub_Data_Array[NumCount+1]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)
#    if NumCount == 9900:
#        if x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount-100]:
#            DangerArray.append(x)
#    if NumCount == 9999:
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount-100]:
#            DangerArray.append(x)
#    elif NumCount > 99 and NumCount not in range(100, 9801, 100) and NumCount not in range (199, 9901, 100) and NumCount < 9900:
#        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount-100] and x < Sub_Data_Array[NumCount+100]:
#            NumCountArray.append(NumCount)
#            DangerArray.append(x)

#for x in DangerArray:
#    FinalAnswer += x+1

#print(FinalAnswer)