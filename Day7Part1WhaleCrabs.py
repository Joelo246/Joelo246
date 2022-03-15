Sub_Data_7 = ("Sub_Data_7.txt")
Sub_String = ""
Sub_Array = []
Tester = 0
Tester2 = 0
FuelCount = 0
FuelCountCheck = 0
LowestNum = 0
HighestNum = 0
RangeCounter = 0
Position = 0

with open(Sub_Data_7) as data_file: #Opens input file and appends it to a string
    for x in data_file:
        Sub_String += x

temp = Sub_String.split(",") #splits and extracts the integers from the string into an array
for x in temp:
    xz = (int(x))
    Sub_Array.append(xz)

#print(Sub_Array)

Sub_Array.sort() #Ordering list and determining its highest and lowest numbers
LowestNum = Sub_Array[0]
HighestNum = Sub_Array[-1]
print(LowestNum)
print(HighestNum)

#print(Sub_Array)
#for x in (range(LowestNum, HighestNum)):
#    print(x)

for x in range(LowestNum, HighestNum): #this sequence Finds the cheapest fuel option
    RangeCounter = RangeCounter+1
    if RangeCounter == 2:
        FuelCountCheck = FuelCount
        Position = Tester
    if RangeCounter > 2: #this sequence checks if its found a cheaper option and if so swaps it in
        if FuelCountCheck < FuelCount:
            pass
        if FuelCountCheck > FuelCount:
            FuelCountCheck = FuelCount
            Position = Tester
    FuelCount = 0
    Tester = int(x)
    for y in Sub_Array: #this part sums all fuel costs for each individual possibility
        Tester2 = int(y)
        if Tester2 > Tester:
            FuelCount += (Tester2 - Tester)
        if Tester > Tester2:
            FuelCount += (Tester - Tester2)
        if Tester == Tester2:
            pass

print("Final Position", Position)
print("Final FuelCount", FuelCountCheck)



