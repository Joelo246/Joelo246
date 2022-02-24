MainDataArray = []
CurrentDepth = 0
CurrentAim = 0
HorizontalPosition = 0
FinalAnswer = 0
SubMovement = "Sub_Data_2.txt"


with open(SubMovement) as data_file: #this loop is to separate the data file into three groups of numbers
        for line in data_file:
            temp_data = line.split(" ")
            if temp_data[0] == "forward":
                HorizontalPosition += int(temp_data[1])
                CurrentDepth += CurrentAim * int(temp_data[1])
            elif temp_data[0] == "down":
                CurrentAim += int(temp_data[1])
            else:
                CurrentAim -= int(temp_data[1])
FinalAnswer = HorizontalPosition * CurrentDepth
print("This should be our current Depth:", CurrentDepth)
print("This should be our current aim", CurrentAim)
print("This should be our Horizontal Position", HorizontalPosition)
print("This should be our Part 2 day 2 Answer:", FinalAnswer)