Sub_Data_8 = ("Sub_Data_8.txt")
Sub_String = ""
Sub_String2 = ""
Sub_String_Input = []
Sub_String_Output = []
ItemCount = 0
OneCount = 0
SevenCount = 0
FourCount = 0
EightCount = 0
FinalAnswer = 0

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

for x in Sub_String_Output:
    if len(x) == 2:
        OneCount = OneCount+1
    if len(x) == 3:
        SevenCount = SevenCount+1
    if len(x) == 4:
        FourCount = FourCount+1
    if len(x) == 7:
        EightCount = EightCount+1

FinalAnswer = OneCount + SevenCount + FourCount + EightCount
print("One Count = ", OneCount)
print("Seven Count = ", SevenCount)
print("Four Count = ", FourCount)
print("Eight Count = ", EightCount)
print("And the final answer is!", FinalAnswer)


print(Sub_String_Input)
print(Sub_String_Output)