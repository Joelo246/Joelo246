Sub_Data_13 = ("Sub_Data_13.txt")
SubString = ""
FoldingInstructions = ""
Coordinates = []
NewCoords = []
Fold = 0
FullCo = ""
CleanedCoords = []

with open(Sub_Data_13) as data_file:
    for line in data_file:
        SubString += line


temp = SubString.split("\n")
for x in temp:
    if x.startswith("fold"):
        FoldingInstructions += x + "\n" #separating the folding instructions from the base coordinates
    else:
        Coordinates.append(x)

Coordinates.pop()

temp = FoldingInstructions.split("\n")
for First, y in enumerate(temp):
    if First == 0:
        if y.startswith("fold along x"): #first fold finds every item below the fold line and does the math to create its new coordinate
            temp2 = y.split("=")
            for z in temp2:
                if z.isdigit() == True:
                    m = int(z)
                    for x in Coordinates:
                        temp3 = str(x)
                        temp4 = temp3.split(",")
                        ItemCount = 0
                        FullCo = ""
                        for l in temp4:
                            ItemCount = ItemCount+1
                            if ItemCount == 1:
                                if int(l) > int(m):
                                    Fold = ((int(m) - int(l)) * 2) + int(l)
                                    FullCo = str(Fold) + ","
                                else:
                                    FullCo = str(l) + ","
                            if ItemCount == 2:
                                FullCo += str(l)
                                NewCoords.append(FullCo)
    if First > 0:
        Coordinates = []
        for x in NewCoords:
            if NewCoords.count(x) == 1:
                CleanedCoords.append(x)
            if NewCoords.count(x) > 1:
                if x not in CleanedCoords:
                    CleanedCoords.append(x) #every fold after we clean the array of duplicate coordinates and then run the math for the new folds
        NewCoords = []
        for x in CleanedCoords:
            Coordinates.append(x)
        CleanedCoords = []
        if y.startswith("fold along x"):
            temp2 = y.split("=")
            for z in temp2:
                if z.isdigit() == True:
                    m = int(z)
                    for x in Coordinates:
                        temp3 = str(x)
                        temp4 = temp3.split(",")
                        ItemCount = 0
                        FullCo = ""
                        for l in temp4:
                            ItemCount = ItemCount+1
                            if ItemCount == 1:
                                if int(l) > int(m): #this checks if the coordinate is after the fold line and needs to be 'folded'
                                    Fold = ((int(m) - int(l)) * 2) + int(l)
                                    FullCo = str(Fold) + ","
                                else:
                                    FullCo = str(l) + ","
                            if ItemCount == 2:
                                FullCo += str(l)
                                NewCoords.append(FullCo)
        if y.startswith("fold along y"):
            temp2 = y.split("=")
            for z in temp2:
                if z.isdigit() == True:
                    m = int(z)
                    for x in Coordinates:
                        temp3 = str(x)
                        temp4 = temp3.split(",")
                        ItemCount = 0
                        FullCo = ""
                        for l in temp4:
                            ItemCount = ItemCount+1
                            if ItemCount == 1:
                                FullCo = str(l)
                            if ItemCount == 2:
                                if int(l) > int(m):
                                    Fold = ((int(m) - int(l)) * 2) + int(l)
                                    FullCo += "," + str(Fold) 
                                    NewCoords.append(FullCo)
                                else:
                                    FullCo += "," + str(l)
                                    NewCoords.append(FullCo)
                            

for x in Coordinates:
    if Coordinates.count(x) == 1:
        CleanedCoords.append(x)
    if Coordinates.count(x) > 1:
        if x not in CleanedCoords:
            CleanedCoords.append(x)

#print("Final answer...", len(CleanedCoords))
#print(CleanedCoords)
CleanedCoords.sort()
print(CleanedCoords)

XArray = []
YArray = []

for x in CleanedCoords:
    temp = x
    temp2 = temp.split(",")
    for count, y in enumerate(temp2):
        if count == 0:
            XArray.append(int(y))
        if count == 1:
            YArray.append(int(y))

print(XArray)
print(YArray)

XTest = range(0, 39)
YTest = range(0, 6)

Matrix = []

for count, i in enumerate(XTest):
    row = []
    for count2, j in enumerate(YTest):
        if (str(i) + "," + str(j)) in CleanedCoords:
            row += "X"
        if (str(i) + "," + str(j)) not in CleanedCoords:
            row += "_"
    Matrix.append(row)

for i in XTest:
    for j in YTest:
        print(Matrix[i][j], end=" ")
    print("")