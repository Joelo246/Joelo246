BinaryData = "Sub_Data_3.txt"
BinaryArray = []
GammaCounter = 0
EpsilonCounter = 0
Temp_Data1 = [] # yup yup yup defining way too many variables cause i'm a rookie ass newb
Temp_Data2 = []
Temp_Data3 = []
Temp_Data4 = []
Temp_Data5 = []
Temp_Data6 = []
Temp_Data7 = []
Temp_Data8 = []
Temp_Data9 = []
Temp_Data10 = []
Temp_Data11 = []
Temp_Data12 = []
Dig1Count = 0
Dig0Count = 0
FinalAnswer = []
FinalAnswerString = str("")
ReverseAnswerString = str("")

with open(BinaryData) as data_file: #This basically jams each of the 12 digits of every line into a different array
    for line in data_file:
        Temp_Data1 += line[0]
        Temp_Data2 += line[1]
        Temp_Data3 += line[2]
        Temp_Data4 += line[3]
        Temp_Data5 += line[4]
        Temp_Data6 += line[5]
        Temp_Data7 += line[6]
        Temp_Data8 += line[7]
        Temp_Data9 += line[8]
        Temp_Data10 += line[9]
        Temp_Data11 += line[10]
        Temp_Data12 += line[11]

for x in Temp_Data1: #each of these blocks counts the 1s and 0s in each digit set and then appends a  
    if x == "1":      #final 1 or 0 to the answer based on which there are more of
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data2:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data3:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data4:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data5:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data6:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data7:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data8:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data9:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data10:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data11:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

for x in Temp_Data12:
    if x == "1":
        Dig1Count = Dig1Count+1
    elif x == "0":
        Dig0Count = Dig0Count+1
if Dig1Count > Dig0Count:
    FinalAnswer.append(1)
    FinalAnswerString += "1"
    ReverseAnswerString += "0"
    Dig1Count = 0
    Dig0Count = 0
if Dig0Count > Dig1Count:
    FinalAnswer.append(0)
    FinalAnswerString += "0"
    ReverseAnswerString += "1"
    Dig1Count = 0
    Dig0Count = 0

print("The gamma rate is", FinalAnswer)
print("Gamma Answer Binary:", FinalAnswerString)
print("Epsilon Answer Binary:", ReverseAnswerString)

GammaCounter = int(FinalAnswerString, 2)
EpsilonCounter = int(ReverseAnswerString, 2)

print("Gamma Decimal Answer:", GammaCounter)
print("Epsilon Decimal Answer:", EpsilonCounter)

FinalFinalAnswer = GammaCounter * EpsilonCounter

print("Submarine Power Consumption issss...:", FinalFinalAnswer)

#print("Number of 1s line 1", Dig1Count)
#print("Number of 0s line 1", Dig0Count)
#print("First data set", Temp_Data1)
#print("hTird data set", Temp_Data3)
#print("Twelth data set", Temp_Data12)
                





