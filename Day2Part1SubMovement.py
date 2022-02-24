import string
import re
# setting up all variables
SubMovement = "Sub_Data_2.txt"
DownArray = []
DownArrayNumbers = []
UpArray = []
ForwardArray = [] #these will load and store our input data
ForwardCount = 0
UpCount = 0
DownCount = 0 #these three will hold all our compiled totals
CurrentDepth = 0 #downcount minus upcount
LineCount = 0 # this one is just for error checks
FinalAnswer = 0

with open(SubMovement) as data_file: #this loop is to separate the data file into three groups of numbers
        for line in data_file:
            if line.startswith("down"):
                m = re.findall('[0-9]', line)
                for item in m:
                    DownArray.append(int(item))
                    LineCount = LineCount+1
#                while line not in string.digits:
#                    def check(line):
#                        for letter in line:
#                            if letter not in string.digits:
#                                del(letter)                
            if line.startswith("up"):
                u = re.findall(r'[0-9]', line)
                for itemu in u:
                    UpArray.append(int(itemu))
                    LineCount = LineCount+1
            if line.startswith("forward"):
                f = re.findall(r'[0-9]', line)
                for itemf in f:
                    ForwardArray.append(int(itemf))
                    LineCount = LineCount+1
 
print(DownArray)
print(UpArray)
print(ForwardArray)
print("Here's the total line count!", LineCount)
#DownArrayNumbers = [int(DownArray, base=16) for num in DownArray]
DownCount = sum(DownArray)
UpCount = sum(UpArray)
ForwardCount = sum(ForwardArray)
print("Here's the total DownCount!", DownCount)
print("Here's the total Upcount!", UpCount)
print("Here's the total ForwardCount!", ForwardCount)
CurrentDepth = (DownCount - UpCount)
print("Current Depth (Down minus up)", CurrentDepth)
FinalAnswer = (ForwardCount * CurrentDepth)
print("Forward multiplied by depth!", FinalAnswer)

#def check(DownArray):
#    for letter in DownArray:
#        if letter not in string.digits:
#            del(letter)
#print(DownArray)



#DownArray.replace({down:''})
# print(DownArray)
#for line in DownArray:
#    DownArrayNumbers.append(int(line))
#print(DownArrayNumbers)

# print(DownArrayNumbers)

# for character, value in enumerate(DownArray):
#    if >= 0:
#        DownArrayNumbers.append(value)

#TempDown = re.findall(r'\d+', DownArray)
#DownArrayNumbers = list(map(int, TempDown))

# for x in DownArray:
 #   if DownArray == "down":
 #       DownArray.remove("down")
                
    #        print(line)
   #         SubMovementArray.append(str(line))
      #  TestLines = data_file.readline()
       # while TestLines:
        #    TestLines = data_file.readline()
         #   LineCount = LineCount+1
          #  for line in TestLines:
           #     SubMovementArray.append(str(TestLines))
#print(SubMovementArray)
#print(LineCount)
            
