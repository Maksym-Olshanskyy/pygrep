import sys

inputText = []
findString = "hello"

def printArr():
    print('Input is:')
    for i in inputText: 
        print(i)

#read & store each line as individual item in list
while True:
        try:
            inputText.append(input())
        except EOFError:
            # no more information
            break


printArr()

for i in range(len(inputText)): # for each line in inputText
    currLine = inputText[i]
    stringLen = len(findString)
    stringIndex = 0
    foundString = False

    for j in range(len(currLine)): # for each char in line
        if currLine[j] == findString[stringIndex]:
            stringIndex += 1
        else:
            stringIndex = 0
        if stringIndex >= stringLen:
            foundString = True
            print("Index " + str(j - stringLen + 1) + " - " + str(j) + ", ", end="")
            stringIndex = 0
    
    if foundString:
        print(inputText[i])
        foundString = False

print()
     
