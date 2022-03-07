Bingo_Inputs = ("Bingo_Inputs.txt")
Bingo_Boards = ("Sub_Data_4.txt")
DrawnNumbers = []
Boards = []
DrawnNumbersStr = ''
BoardsStr = ''
BoardsStr2 = ''
BoardHits = 0
Bad_Chars = ['\n'] #I'm a veritable variable mess
TempInt = 0
TempStr = ''
TempBoard = ''
BingoChecker = ''
BingoCheck2 = ''
BingoCheck3 = []
TempStrArray = []
ItemCount = 0
RowCount = 0
LineCount = 0
MasterLineCount = 0 #I'm a veritable variable mess
MasterLineCount2 = 0
MasterBoardCount = 0
BoardStart = 0
BoardEnd = 0
BoardCount = 1
FinalBoard = ""
FinalArray = []
FinalBoardSum = 0
FinalNumberCall = 0
FinalAnswer = 0
Victory = False
Col1 = 0
Col2 = 0
Col3 = 0
Col4 = 0
Col5 = 0 #I'm a veritable variable mess
Diag1 = 0
Diag2 = 0
Row1 = 0
Row2 = 0
Row3 = 0
Row4 = 0
Row5 = 0

y = ''
n = 75 # I made this to try to divide my board by groups of 75 characters, didn't work.
TempArray = []
DigitChecker = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class style: #this is here to try to bold characters for my code
    BOLD = '\033[1m'
    BOLDEND = '\033[0m'

from cgi import test #I can't even remember what I was tring to do with these
from operator import truediv #I can't even remember what I was tring to do with these
import re #this one i like and use a lot
from itertools import zip_longest # this one worked for dividing the board but wasn't necessary

with open(Bingo_Inputs) as data_file: #this loop is to read the list of inputs into an array
    for x in data_file:
        temp = re.split(',', x)
        for item in temp:
            DrawnNumbers.append(item)
temp.clear()

with open(Bingo_Boards) as data_file2: #this loop takes out the \n line breaks to clean up the group and then moves just the integers to Boards
    for line in data_file2:
#        BoardsStr += line = # changing to add this variable later
        line = ''.join((filter(lambda i: i not in Bad_Chars, line)))
        temp += re.split(' ', line)
    for item in temp:
        if item.isdigit():
            Boards.append(item) #going back and forth on making this an int or not
temp.clear()

for x in range(len(Boards)): #this finds every number under 10 and adds a 0 to the start of it - successfully!
    TempInt = (int(Boards[x]))
    if TempInt < 10:
        if Boards[x] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            Boards[x] = "0" + Boards[x]
        TempInt = 0
    else:
        TempInt = 0
        continue
# print(Boards)

for x in range(len(DrawnNumbers)): #this finds every number under 10 and adds a 0 to the start of it - successfully!
    TempInt = (int(DrawnNumbers[x]))
    if TempInt < 10:
        if DrawnNumbers[x] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            DrawnNumbers[x] = "0" + DrawnNumbers[x]
        TempInt = 0
    else:
        TempInt = 0
        continue
# print(Boards)
# print(DrawnNumbers)

for item in Boards: #this converts the boards array back into bingo board shapes
    if ItemCount <= 3 and RowCount <= 4: #inserts items from boards into boardstring
        BoardsStr += item + " "
        ItemCount = ItemCount+1
    elif ItemCount > 3 and RowCount <= 4:
        BoardsStr += item + " " + "\n" #checks every 5 items and adds a line break
        ItemCount = 0
        RowCount = RowCount+1
    elif RowCount > 4:
        BoardsStr += "\n" + item + " " # Checks every 5 line breaks and adds a blank line
        RowCount = 0
        ItemCount = ItemCount+1

BingoChecker = BoardsStr

for x in DrawnNumbers: # This little bit of code finds and bolds each match between DrawnNumbers and BoardStr
    TempStr += x
    BoardsStr = BoardsStr.replace(TempStr, style.BOLD + TempStr + style.BOLDEND) #Numbers bolded as they're called
    BingoChecker = BingoChecker.replace(TempStr, "XY") #Secondary array to check for winners
    TempStr = ""
    lines = BingoChecker.split("\n") # Splits this baby into lines to be combed over
    if Victory == True: # If a bingo is hit this should bust us out of the for loop before every single digit is bolded
        break
    for line in lines:
        MasterLineCount = MasterLineCount+1 # This helps to find where the bingo is
        if LineCount < 6: # This line count to 6 ensures we only ever look at one board at a time
            TempBoard += line + "\n"
            LineCount = LineCount+1
            if line.find("XY", 0, 2) == 0: # Next 5 if statements basically check that the number has been replaced with XY
                Col1 = Col1+1              # And if so, they add a point counter to any row, column, or diagonal they intersect with
                Row1 = Row1+1
                if LineCount == 1:
                    Diag1 = Diag1+1
                if LineCount == 5:
                    Diag2 = Diag2+1
            if line.find("XY", 3, 5) == 3:
                Col2 = Col2+1
                Row2 = Row2+1
                if LineCount == 2:
                    Diag1 = Diag1+1
                if LineCount == 4:
                    Diag2 = Diag2+1
            if line.find("XY", 6, 8) == 6:
                Col3 = Col3+1
                Row3 = Row3+1
                if LineCount == 3:
                    Diag1 = Diag1+1
                    Diag2 = Diag2+1
            if line.find("XY", 9, 11) == 9:
                Col4 = Col4+1
                Row4 = Row4+1
                if LineCount == 4:
                    Diag1 = Diag1+1
                if LineCount == 2:
                    Diag2 = Diag2+1
            if line.find("XY", 12, 14) == 12:
                Col5 = Col5+1
                Row5 = Row5+1
                if LineCount == 1:
                    Diag2 = Diag2+1
                if LineCount == 5:
                    Diag1 = Diag1+1
            if Row1 and Row2 and Row3 and Row4 and Row5 == 1: # This checks if after one line the entire row column is filled with XY's
                MasterLineCount2 = MasterLineCount % 600 # Whole data set is 600 lines, so the remainder of this divided by 600 gives us the actual line count
                MasterBoardCount = MasterLineCount2 // 6 # And that line count divided by 6 should give us which bingo board we're on
                FinalNumberCall = int(x) #Saving this number for later
                print("Huzzah, we found a bingo row!\n", TempBoard)
                print(f"And it was located line: {MasterLineCount2} of board: {MasterBoardCount}")
                print("And the last number called was:", x)
                print(f"And the linecount at the time was: {LineCount}")
                Victory = True
            else: # Resets the row column only, since the diagonal and column variables must count over multiple lines
                Row1 = 0
                Row2 = 0
                Row3 = 0
                Row4 = 0
                Row5 = 0
            if (Col1 == 5) or (Col2 == 5) or (Col3 == 5) or (Col4 == 5) or (Col5 == 5): # Checks if any columns have found 5 XY matches
                MasterLineCount2 = MasterLineCount % 600
                MasterBoardCount = MasterLineCount2 // 6
                FinalNumberCall = int(x)
                print("Hurrah, we found a bingo column!\n", TempBoard)
                print(f"And it was located line: {MasterLineCount2} of board: {MasterBoardCount}")
                print("And the last number called was:", x)
                print(f"And the linecount at the time was: {LineCount}")
                print(Col1)
                print(Col2)
                print(Col3)
                print(Col4)
                print(Col5)
                Victory = True
            if (Diag1 == 5) or (Diag2 == 5): # Checks if any diagonals have found 5 XY matches
                MasterLineCount2 = MasterLineCount % 600
                MasterBoardCount = MasterLineCount2 // 6
                FinalNumberCall = int(x)
                print("Hutz'pah, we count a bingo diagonal!\n", TempBoard)
                print(f"And it was located line: {MasterLineCount2} of board: {MasterBoardCount}")
                print("And the last number called was:", x)
                print(f"And the linecount at the time was: {LineCount}")
                Victory = True
        if Victory == True:
            break
        if LineCount == 6:
            LineCount = 0
            TempBoard = ""
            Row1 = 0
            Row2 = 0
            Row3 = 0
            Row4 = 0
            Row5 = 0
            Col1 = 0
            Col2 = 0
            Col3 = 0
            Col4 = 0
            Col5 = 0
            Diag1 = 0
            Diag2 = 0
            BoardCount = BoardCount+1

print("And now for a little cleanup")
print(f"If out bingo was on line: {MasterLineCount2} and we were on line {LineCount} at the time, then our array should run from...")
BoardStart = MasterLineCount2 - LineCount
BoardEnd = BoardStart + 5
print(f"...a start of line {BoardStart} and and end of line {BoardEnd}")
print("Lets check out just that board")
LineCount = 0
lines = ""
lines = BingoChecker.split("\n")
for line in lines:
    LineCount = LineCount+1
    if LineCount < BoardStart:
        continue
    if LineCount >= BoardStart and LineCount <= BoardEnd:
        FinalBoard += line + "\n"
    if LineCount > BoardEnd:
        break
print("This should be our final board!\n", FinalBoard)
print("So lets find the sum of uncalled numbers!")
numbers = ""
numbers = FinalBoard.split()
for number in numbers:
    if number == "XY":
        continue
    else:
        FinalArray.append(int(number))
print("This Should be all the numbers", FinalArray)
FinalBoardSum = sum(FinalArray)
print("This Should be the remaining numbers summed!", FinalBoardSum)
FinalAnswer = (FinalBoardSum*FinalNumberCall)
print(f"And Multiplying that sum - {FinalBoardSum} by the final number called - {FinalNumberCall} should give us a Final answer of: {FinalAnswer} !!")
print("Okay whats going on here", FinalNumberCall)
print(FinalAnswer)
print(FinalBoardSum)
print(type(FinalBoardSum))
print(type(FinalNumberCall))
print(type(FinalAnswer))

# DrawnNumbersStr = "95 87 83 87 XY "
#tester = DrawnNumbersStr.find("XY", 12, 14)
#print(tester)
#print(Col1)
#print(Col2)
#print(Col3)
#print(Col4)
#print(Col5)
#    for line in BoardsStr:
#print(BingoChecker)
#print(BoardsStr)
#print(len(BingoCheck2))
# print(BingoCheck3)
# print(BoardsStr)
#print(BingoChecker)

#def grouper(iterable, count, fillvalue=None): #attempting to use an outside tool to step through my Boards Array in 25s
#    args = [iter(iterable)] * count
#    return zip_longest(*args, fillvalue=fillvalue)

#for x in grouper(BoardsStr, 25, ""): #this code works to make x groups of 75, ie boards, but I'm not sure what to do from here
#    print(x)
#    print(TempStr)

#for x in TempStr:
#    BoardsStr2 += x
# print(BoardsStr2)



#print(BoardsStr)



#for x in grouper(BoardsStr, 25, ""): #this code works to make x groups of 25, ie boards, but I'm not sure what to do from here
#    TempArray = x
        


#        TempStr = str(TempInt)
#        TempStr = "0" + TempStr
#        print(TempStr)
#        Boards[x] = TempStr
#    else:
#        continue



#    if x == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
#        x = "0" + x
#        print(x)

#print(DrawnNumbers)
#print(Boards)



#if DrawnNumbers[3] in BoardsStr: #this whole block was built to try to bold the correct part of the bingo board string, but setting it aside for now
#    TempStr += DrawnNumbers[3]
#    if re.fullmatch(r'\d{1}', TempStr) == None:
#        BoardsStr = BoardsStr.replace(TempStr, style.BOLD + TempStr + style.BOLDEND)
#    else:
#        TempStrArray.append(TempStr + '\d')
#        TempStrArray.append('\d' + TempStr)
#        print(TempStrArray)
#        for i in range(len(BoardsStr)):
#            print(i[+1])
#            if i+i[+1] == TempStr + " " and not "\d" + TempStr:
#                BoardsStr = BoardsStr.replace(i, style.BOLD + TempStr + style.BOLDEND)
#            elif i+[i-1] == " " + TempStr and not TempStr + "\d":
#                BoardsStr = BoardsStr.replace(i, style.BOLD + TempStr + style.BOLDEND)
#            elif [i-1]+i+[i+1] == " " + TempStr + " ":
#                BoardsStr = BoardsStr.replace(i, style.BOLD + TempStr + style.BOLDEND)
#        tempmatch = re.search(TempStr + '\d{1}' or '\d{1}' + TempStr, BoardsStr)
#        print("whats this showin?", tempmatch)
#        y += tempmatch.group()
#        print("whats this showin?", y)
#        for item in tempmatch:
#            TempArray.append(tempmatch.group)
#        if TempStr not in TempArray:
#            BoardsStr = BoardsStr.replace(TempStr, style.BOLD + TempStr + style.BOLDEND)
        
            

#print(BoardsStr)
#print(TempStr)
#print(DrawnNumbers[3])

#for x in DrawnNumbers:
#    if x in Boards:
#        Boards.insert(x, x+100)
#        BoardHits = BoardHits+1

#print("Board Hits!",BoardHits)
#print("ArrayCount!", len(DrawnNumbers))
#print(DrawnNumbers)
#print(Boards)



#for line in BoardsStr:
#    temp = re.split(" ", line)
#    for item in temp:
#        BoardsStr2 += item


#for x in DrawnNumbers:
#    if x == re.match(x, BoardsStr):
#        BoardsStr = BoardsStr.replace(x, style.BOLD + x + style.BOLDEND)

#print("Come on work BOLDies!", Boards)
#print("Come on work BOLDies??!", DrawnNumbers)

#Test = 'hello'
#print("test1", Test)
#print("test2", style.BOLD + Test + style.BOLDEND)
#Test = style.BOLD + Test + style.BOLDEND
#print("test3", Test)
# print(BoardsStr)
# print(BoardsStr)


#BoardsStr = (str(Boards))
#DrawnNumbersStr = (str(DrawnNumbers))

#for x in DrawnNumbers:
#    if x[1] in Boards:
#        Boards = Boards.replace(x[1], 'X')

#print("string work?", DrawnNumbersStr)
#print("string Work?", BoardsStr)
#print("String WORK", Boards)

#        temp = ''.join(i for i in temp if not i in Bad_Chars)