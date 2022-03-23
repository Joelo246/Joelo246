Sub_Data_11 = ("Sub_Data_11.txt")
SubString = ""
Sub_Array = []
StepCount = 0
IndexCount = -1
NoHitter = 0
FlashCounter = 0
PulseArray = []
LeftWall = [10, 20, 30, 40, 50, 60, 70, 80]
RightWall = [19, 29, 39, 49, 59, 69, 79, 89]
Top = [1, 2, 3, 4, 5, 6, 7, 8]
Bottom = [91, 92, 93, 94, 95, 96, 97, 98]
AllExcept = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
BabyFlashCounter = 0

with open(Sub_Data_11) as data_file:
    for x in data_file:
        SubString += x

Temp = SubString.split("\n") #the usual, opening the file, tossing it into an integer array
for x in Temp:
        for y in x:
            Sub_Array.append(int(y))

while StepCount < 1000: #this fills the requirement of running program fro 100 steps
    StepCount = StepCount+1
    IndexCount = -1
    PulseArray = []
    for x in Sub_Array:               #this does part 1 of step 1 - adding 1 to every item
        IndexCount = IndexCount+1
        Sub_Array[IndexCount] = x+1
    NoHitter = 1
    while NoHitter > 0:                 #This is the trickier section, locating each item 10 and up and having it "pulse" --
        NoHitter = 0                    # -- an additional number onto everything around it, then rechecking everything for new 10s
        IndexCount = -1 
        for x in Sub_Array:
            IndexCount = IndexCount+1
            if IndexCount == 0:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+11] = Sub_Array[IndexCount+11]+1
            if IndexCount in Top:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1          #different blocks to check indexes based on whether they are
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1          #in a corner, wall, or center
                    Sub_Array[IndexCount+9] = Sub_Array[IndexCount+9]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+11] = Sub_Array[IndexCount+11]+1
            if IndexCount == 9:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+9] = Sub_Array[IndexCount+9]+1
            if IndexCount in LeftWall:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount-9] = Sub_Array[IndexCount-9]+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+11] = Sub_Array[IndexCount+11]+1
            if IndexCount in RightWall:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount-11] = Sub_Array[IndexCount-11]+1
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+9] = Sub_Array[IndexCount+9]+1
            if IndexCount in Bottom:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1
                    Sub_Array[IndexCount-9] = Sub_Array[IndexCount-9]+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount-11] = Sub_Array[IndexCount-11]+1
            if IndexCount == 90:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1
                    Sub_Array[IndexCount-9] = Sub_Array[IndexCount-9]+1
            if IndexCount == 99:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1
                    Sub_Array[IndexCount-11] = Sub_Array[IndexCount-11]+1
            elif IndexCount not in AllExcept:
                if x > 9 and IndexCount not in PulseArray:
                    PulseArray.append(IndexCount)
                    FlashCounter = FlashCounter+1
                    NoHitter = NoHitter+1
                    Sub_Array[IndexCount+1] = Sub_Array[IndexCount+1]+1
                    Sub_Array[IndexCount-1] = Sub_Array[IndexCount-1]+1
                    Sub_Array[IndexCount-9] = Sub_Array[IndexCount-9]+1
                    Sub_Array[IndexCount-10] = Sub_Array[IndexCount-10]+1
                    Sub_Array[IndexCount-11] = Sub_Array[IndexCount-11]+1
                    Sub_Array[IndexCount+9] = Sub_Array[IndexCount+9]+1
                    Sub_Array[IndexCount+10] = Sub_Array[IndexCount+10]+1
                    Sub_Array[IndexCount+11] = Sub_Array[IndexCount+11]+1
    IndexCount = -1
    for x in Sub_Array:                    #after all the pulses are complete, change everything over 9 to 0, then start again on the next step
        IndexCount = IndexCount+1
        if x > 9:
            BabyFlashCounter = BabyFlashCounter+1
            Sub_Array[IndexCount] = 0
        else:
            pass
    if BabyFlashCounter == 100:
        print("Everything will flash on step...", StepCount)
    BabyFlashCounter = 0


print("Final Answer is hopefully...!", FlashCounter)

