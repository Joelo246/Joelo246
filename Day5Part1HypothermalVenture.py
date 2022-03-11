Sub_Data_5 = ("Sub_Data_5.txt")
Sub_Data_String = ""
NumCount = 0
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
AllHits = []
TempStr = ""
CheckArray = []
DangerZone = 0





with open(Sub_Data_5) as temp_data:
    for line in temp_data:
        Sub_Data_String += line

for line in Sub_Data_String:
    Sub_Data_String = Sub_Data_String.replace(" -> ", ",")
    Sub_Data_String = Sub_Data_String.replace("\n", ",") #open files and clean them of weird characters, adding consistent comma between every number

temp = Sub_Data_String.split(",") #split the file by commas to reach each number
for x in temp:
    NumCount = NumCount+1 #break the numbers into groups of 4 and assign each to an integer
    if NumCount == 1:
        Num1 = int(x)
    if NumCount == 2:
        Num2 = int(x)
    if NumCount == 3:
        Num3 = int(x)
    if NumCount == 4:
        Num4 = int(x)
        NumCount = 0
        if Num1 == Num3: #append their list of coordinates to the array
            if Num2 < Num4:
                for x in range(Num2, Num4+1):
                    TempStr = str(Num1) + "," + str(x)
                    if (TempStr in AllHits) and (TempStr not in CheckArray):
                        CheckArray.append(TempStr)
                    AllHits.append(TempStr)
            if Num4 < Num2:
                for x in range(Num4, Num2+1):
                    TempStr = str(Num1) + "," + str(x)
                    if (TempStr in AllHits) and (TempStr not in CheckArray):
                        CheckArray.append(TempStr)
                    AllHits.append(TempStr)   
        if Num2 == Num4: #append their list of coordinates to the array
            if Num1 < Num3:
                for x in range(Num1, Num3+1):
                    TempStr = str(x) + "," + str(Num2)
                    if (TempStr in AllHits) and (TempStr not in CheckArray):
                        CheckArray.append(TempStr)
                    AllHits.append(TempStr)
            if Num3 < Num1:
                for x in range(Num3, Num1+1):
                    TempStr = str(x) + "," + str(Num2)
                    if (TempStr in AllHits) and (TempStr not in CheckArray):
                        CheckArray.append(TempStr)
                    AllHits.append(TempStr)       
        else:
            continue

#print(AllHits)

DangerZone = len(CheckArray)
print(DangerZone)

# print(temp)    
#    for x in temp:
#        print(x)

