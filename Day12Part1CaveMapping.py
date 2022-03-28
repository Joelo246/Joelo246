Sub_Data_12 = ("Sub_Data_12.txt")
PathArray = []
SmallCaves = []
StartArray = []
New_Path_Array = []
New_Path = ""
temp = ""
ItemCount = 0
Options = []
NewPathCount = 0
AllFullPaths = []
AllDeadPaths = []
LastPathCount = 0
DoneArray = []
HitCount = 0
MissCount = 0
tempertemper =  []

with open(Sub_Data_12) as data_file:
    for line in data_file:
        temp = line.strip("\n")
        y = temp.startswith("start")
        if y == True:
            StartArray.append(temp)
        if y == False:
            PathArray.append(temp)
        temp2 = temp.split("-")
        for x in temp2:
            if x.islower() == True:
                if x not in SmallCaves:
                    SmallCaves.append(x)
for x in StartArray:
    if len(DoneArray) == 3:
        break
    if x not in DoneArray:
        New_Path_Array = []
        temp = x
        temp2 = temp.split("-")
        for y in temp2:
            New_Path_Array.append(y)
        NewPathCount = 0
        TwoPathCount = 0

        while NewPathCount == 0:
            for firstcount, z in enumerate(PathArray):
#                print("Talk to me, yo", New_Path_Array)
                New_Path = ""    
                temp = z
                temp2 = temp.split("-")
                HitCount = 0
#                if New_Path_Array == []:
#                    print("I think this starter is exhausted")
#                    DoneArray.append(x)
#                    NewPathCount = NewPathCount+1
#                    break
                if len(New_Path_Array) <= 1:
                    print("I think this starter is exhausted")
                    DoneArray.append(x)
                    NewPathCount = NewPathCount+1
                    break
#                if "start-tf-" in AllDeadPaths:
#                    print("I think this starter is exhausted")
#                    DoneArray.append(x)
#                    NewPathCount = NewPathCount+1
#                    break
#                if "start-EU-" in AllDeadPaths:
#                    print("I think this starter is exhausted")
#                    DoneArray.append(x)
#                    NewPathCount = NewPathCount+1
#                    break
                for count, temp22 in enumerate(temp2):
                    if count == 0:
                        if temp22 == New_Path_Array[-1] and HitCount == 0:
                            if temp2[count+1] not in SmallCaves:
                                for x in New_Path_Array:
                                    New_Path += x + "-"
                                New_Path += temp2[count+1] + "-"
                                if New_Path not in AllDeadPaths and New_Path not in AllFullPaths:
                                    New_Path_Array.append(temp2[count+1])
                                    HitCount = HitCount+1
                                    MissCount = 0
                                if New_Path in AllDeadPaths or New_Path in AllFullPaths:
                                    pass
#                                    print("Dead end, keep goin'")
                            if temp2[count+1] in SmallCaves:
                                if temp2[count+1] in New_Path_Array:
                                    pass
                                elif temp2[count+1] not in New_Path_Array:
                                    for x in New_Path_Array:
                                        New_Path += x + "-"
                                    New_Path += temp2[count+1] + "-"
                                    if New_Path not in AllDeadPaths and New_Path not in AllFullPaths:
                                        New_Path_Array.append(temp2[count+1])
                                        HitCount = HitCount+1
                                        MissCount = 0
                                    if New_Path in AllDeadPaths or New_Path in AllFullPaths:
                                        pass
#                                        print("Dead end, keep goin'")
                        elif temp22 != New_Path_Array[-1]:
                            pass
#                            MissCount = MissCount+1
                    New_Path = ""
                    if count == 1:
                        if temp22 == New_Path_Array[-1] and HitCount == 0:
                            if temp2[count-1] not in SmallCaves:
                                for x in New_Path_Array:
                                    New_Path += x + "-"
                                New_Path += temp2[count-1] + "-"
                                if New_Path not in AllDeadPaths and New_Path not in AllFullPaths:
                                    New_Path_Array.append(temp2[count-1])
                                    HitCount = HitCount+1
                                    MissCount = 0
                                if New_Path in AllDeadPaths or New_Path in AllFullPaths:
                                    pass
#                                    print("Dead end, keep goin'")
                            if temp2[count-1] in SmallCaves:
                                if temp2[count-1] in New_Path_Array:
                                    pass
                                elif temp2[count-1] not in New_Path_Array:
                                    for x in New_Path_Array:
                                        New_Path += x + "-"
                                    New_Path += temp2[count-1] + "-"
                                    if New_Path not in AllDeadPaths and New_Path not in AllFullPaths:
                                        New_Path_Array.append(temp2[count-1])
                                        HitCount = HitCount+1
                                        MissCount = 0
                                    if New_Path in AllDeadPaths or New_Path in AllFullPaths:
                                        pass
#                                        print("Dead end, keep goin'")
                        elif temp22 != New_Path_Array[-1]:
                            pass
#                            MissCount = MissCount+1
                New_Path = ""
                if HitCount == 0:
                    MissCount = MissCount+1
                if New_Path_Array[-1] == "end":
                    New_Path = ""
                    for x in New_Path_Array:
                        New_Path += x + "-"
                    if New_Path not in AllFullPaths:
                        AllFullPaths.append(New_Path)
                        print("New Path Found!", New_Path)
                    if New_Path not in AllFullPaths:
                        AllFullPaths.append(New_Path)
                        New_Path_Array.pop()
                if MissCount == 2*(len(PathArray)):
#                        print("Damn I think we're stuck!")
                    for x in New_Path_Array:
                        New_Path += x + "-"
                    if New_Path not in AllDeadPaths:
                        AllDeadPaths.append(New_Path)
#                        print("New Dead End Found!", New_Path)
                    New_Path_Array.pop()
                    MissCount = 0

#        for j in reversed(PathArray):
#            tempertemper.append(j)
#        PathArray = []
#        for x in tempertemper:
#            PathArray.append(x)
#        tempertemper = []




#                if DisCount > 3:
#                   print("Damn I think we're REALLY stuck!")
#                    New_Path_Array.pop()
#                    DisCount = 0
#                    CisCount = CisCount+1
#                if CisCount >3:
#                   print("Damn I think we're REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    CisCount = 0
#                    FriskCount = FriskCount+1
#                if FriskCount >3:
#                        print("Damn I think we're REALLY REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    FriskCount = 0
#                    SwishCount = SwishCount+1
#                if SwishCount >3:
#                        print("Damn I think we're REALLY REALLY REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    SwishCount = 0
#                    BriskCount = BriskCount+1
#                if BriskCount >3:
#                        print("Damn I think we're REALLY REALLY REALLY REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    BriskCount = 0
#                    WhiskCount = WhiskCount+1
#                if WhiskCount >3:
#                        print("Damn I think we're REALLY REALLY REALLY REALLY REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    WhiskCount = 0
#                    GriftCount = GriftCount+1
#                if GriftCount >3:
#                   print("Damn I think we're REALLY REALLY REALLY REALLY REALLY REALLY REALLY stuck!")
#                    print("Here' a fukt erray on 8 deletions", New_Path_Array)
#                    New_Path_Array.pop()
#                    GriftCount = 0
#                    HolyShitCount = HolyShitCount+1
#                if HolyShitCount >3:
#                    print("Damn I think we're REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY REALLY stuck!")
#                    New_Path_Array.pop()
#                    HolyShitCount = 0                
#                    if New_Path in AllFullPaths:
#                       print("Nuh uh, that one aint new, try again", New_Path)
#                        New_Path_Array.pop()
#                        LastPathCount = LastPathCount+1
#                        if LastPathCount > 2:
#                                print("Okay this path seems quite bad try backing up further")
#                            New_Path_Array.pop()
#                            LastPathCount = 0
#                            TwoPathCount = TwoPathCount+1
#                            if TwoPathCount > 2:
#                                    print("Okay this path seems quite bad try backing up further")
#                                New_Path_Array.pop()
#                                TwoPathCount = 0
#                                ThreePathCount = ThreePathCount+1
#                                if ThreePathCount > 2:
#                                        print("Okay this path seems quite bad try backing up further")
#                                    New_Path_Array.pop()
#                                    ThreePathCount = 0
#                                    FourPathCount = FourPathCount+1
#                                    if FourPathCount > 2:
#                                            print("Okay this path seems quite bad try backing up further")
#                                        New_Path_Array.pop()
#                                        FourPathCount = 0
#                                        FivePathCount = FivePathCount+1
#                                        if FivePathCount > 2:
#                                            print("Okay this path seems quite bad try backing up further")
#                                            New_Path_Array.pop()
#                                            FivePathCount = 0
#                                            SixPathCount = SixPathCount+1
#                                            if SixPathCount > 2:
#                                               print("Okay this path seems quite bad try backing up further")
#                                                New_Path_Array.pop()
#                                                SixPathCount = 0
#                                                SevenPathCount = SevenPathCount+1
#                                                if SevenPathCount > 2:                                                    
#                                                    New_Path_Array.pop()
#                                                    SevenPathCount = 0
#                                                    EightPathCount = EightPathCount+1
#                                                    if EightPathCount > 2:        
#                                                        New_Path_Array.pop()
#                                                        EightPathCount = 0
#                                                        NinePathCount = NinePathCount+1
#                                                        if NinePathCount > 2:        
#                                                            New_Path_Array.pop()
#                                                            NinePathCount = 0
#                                                            TenPathCount = TenPathCount+1
#                                                            if TenPathCount > 2:
#                                                                print("Okay this path seems quite bad try backing up further")        
#                                                                New_Path_Array.pop()
#                                                                TenPathCount = 0


                        

                        
                            
print("Okay wtf we got", AllFullPaths)
print("And how many?", len(AllFullPaths))




#for x in PathArray:
#    temp = x
#    temp2 = temp.startswith("start")
#    if temp2 == True:
#        temp2 = temp.split("-")
#        for x in temp2:
#            New_Path_Array.append(x)
#            for x in PathArray:
#                    
#        New_Path += temp
#    print(New_Path)

    
#print(SmallCaves)