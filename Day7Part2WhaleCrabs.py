Sub_Data_7 = ("Sub_Data_7.txt")
Sub_String = ""
Sub_Array = []
Tester = 0
Tester2 = 0
FuelCount = 0
FuelDistance = 0
FuelCountCheck = 0
FuelTotal = 0
LowestNum = 0
HighestNum = 0
RangeCounter = 0
Position = 0
temp = 0
temp2 = 0
temp3 = 0

def Fuel_Counter(x):
    temp2 = 0
    for y in range(0, x):
        temp = y
        temp2 += temp
    temp2 += x
    return temp2


with open(Sub_Data_7) as data_file: #Opens input file and appends it to a string
    for x in data_file:
        Sub_String += x

temp = Sub_String.split(",") #splits and extracts the integers from the string into an array
for x in temp:
    xz = (int(x))
    Sub_Array.append(xz)


Sub_Array.sort() #Ordering list and determining its highest and lowest numbers
LowestNum = Sub_Array[0]
HighestNum = Sub_Array[-1]
print(LowestNum)
print(HighestNum)


for x in range(LowestNum, HighestNum):
    RangeCounter = RangeCounter+1
    if RangeCounter == 2:
        FuelCountCheck = FuelCount
        Position = Tester
    if RangeCounter > 2:
        if FuelCountCheck < FuelCount:
            pass
        if FuelCountCheck > FuelCount:
            FuelCountCheck = FuelCount
            Position = Tester
    FuelCount = 0
    Tester = int(x)
    for y in Sub_Array:
        Tester2 = int(y)
        if Tester2 > Tester:
            FuelDistance = (Tester2 - Tester)
            temp3 = Fuel_Counter(FuelDistance)
            FuelCount += temp3
        if Tester > Tester2:
            FuelDistance = (Tester - Tester2)
            temp3 = Fuel_Counter(FuelDistance)
            FuelCount += temp3
        if Tester == Tester2:
            pass

print("Final Position", Position)
print("Final FuelCount", FuelCountCheck)

#FuelDistance = (15-5)
#RandomVar = Fuel_Counter(FuelDistance)
#print(RandomVar)

