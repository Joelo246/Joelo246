from ast import Sub

Sub_Data_6 = ("Sub_Data_6.txt")
Sub_String = ""
Sub_Array = []
Sub_Array_Temp = []
DayCounter = 0
ArrayCounter = 0




with open(Sub_Data_6) as data_file: #Opens input file and appends it to a string
    for x in data_file:
        Sub_String += x

temp = Sub_String.split(",") #splits and extracts the integers from the string into an array
for x in temp:
    Sub_Array.append(int(x))

print("testin", len(Sub_Array))

while DayCounter <= 80: #main program, attempts to run an 80 day expanding counter of the fish births
    if DayCounter >=1:
        Sub_Array.clear()
        for i in Sub_Array_Temp:
            Sub_Array.append(i)
    Sub_Array_Temp.clear()
    DayCounter = DayCounter+1
    for x in Sub_Array:
        if x == 0:
            Sub_Array_Temp.append(6)
            Sub_Array_Temp.append(8)
        else:            
            Sub_Array_Temp.append(x-1)

print(Sub_Array)
print(len(Sub_Array))
