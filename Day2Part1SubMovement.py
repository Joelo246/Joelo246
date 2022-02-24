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

with open(SubMovement) as data_file: #this loop is to separate the data file into three groups of numbers
        for line in data_file:
            if line.startswith("down"):
                m = re.findall(r'[0-9]', line)
                DownArray.append(m)
                LineCount = LineCount+1
#                while line not in string.digits:
#                    def check(line):
#                        for letter in line:
#                            if letter not in string.digits:
#                                del(letter)
                
            if line.startswith("up"):
                u = re.findall(r'[0-9]', line)
                UpArray.append(u)
                LineCount = LineCount+1
            if line.startswith("forward"):
                f = re.findall(r'[0-9]', line)
                ForwardArray.append(f)
                LineCount = LineCount+1
 
print(DownArray)
print(UpArray)
print(ForwardArray)
print(LineCount)
DownArrayNumbers = int(DownArray)
DownCount = sum(DownArrayNumbers)
UpCount = sum(UpArray)
ForwardCount = sum(ForwardArray)
print(DownCount)
print(UpCount)
print(ForwardCount)

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
            
