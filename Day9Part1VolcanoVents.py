Sub_Data = ("Sub_Data_9.txt")
Sub_Data_String = ""
Sub_Data_Array = []
NumCount = 0
DangerArray = []
FinalAnswer = 0
NumCountArray = []

with open(Sub_Data) as Data_File:
    for line in Data_File:
        Sub_Data_String += line

for x in Sub_Data_String: #open files and clean them of weird characters, adding consistent comma between every number
    Sub_Data_String = Sub_Data_String.replace("\n", "")

for x in Sub_Data_String:
    Sub_Data_Array.append(int(x))

NumCount = -1

for x in Sub_Data_Array:
    NumCount = NumCount+1
    if NumCount == 0:
#        print(NumCount)
        if x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount+100]:
#            print(Sub_Data_Array[NumCount+1])
#            print(Sub_Data_Array[NumCount+100])
#            print("Found one!", x)
            DangerArray.append(x)
    if NumCount > 0 and NumCount < 99:
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount+100]:
#            print("This my numba", x)
#            print("This its item", NumCount)
#            print(Sub_Data_Array[NumCount+1])
#            print(Sub_Data_Array[NumCount+100])
#            print(Sub_Data_Array[NumCount-1])
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)
    if NumCount == 99:
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+100]:
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)
    if NumCount in range(100, 9801, 100):
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount+100] and x < Sub_Data_Array[NumCount-100]:
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)
    if NumCount in range (199, 9901, 100):
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+100] and x < Sub_Data_Array[NumCount-100]:
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)
    if NumCount > 9900 and NumCount < 9999:
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount-100] and x < Sub_Data_Array[NumCount+1]:
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)
    if NumCount == 9900:
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount-100]:
#            print("Found one!", x)
            DangerArray.append(x)
    if NumCount == 9999:
#        print(NumCount)
#        print(x)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount-100]:
#            print("Found one!", x)
            DangerArray.append(x)
    elif NumCount > 99 and NumCount not in range(100, 9801, 100) and NumCount not in range (199, 9901, 100) and NumCount < 9900:
#        print(NumCount)
#        print(x)
#        print("What indexes we seeing here", NumCount)
        if x < Sub_Data_Array[NumCount-1] and x < Sub_Data_Array[NumCount+1] and x < Sub_Data_Array[NumCount-100] and x < Sub_Data_Array[NumCount+100]:
#            print("Found one item..", NumCount)
            NumCountArray.append(NumCount)
            DangerArray.append(x)

dups = [x for x in NumCountArray if NumCountArray.count(x) > 1]
print(dups)

for x in DangerArray:
    FinalAnswer += x+1

print(sum(DangerArray))
print(len(DangerArray))

#print("Now wtf is in here??", NumCountArray)
#print(DangerArray)
print(FinalAnswer)
