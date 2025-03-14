import sys

inputText = []
findString = "hello"
print(str(len(findString)))

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
stringLen = len(findString)
print("Output is: ")
for i in range(len(inputText)): # for each line in inputText
    currLine = inputText[i]
    
    foundString = True
    printLine = False

    #for j in range(): # for each char in line
    j = 0
    while j <= len(currLine) - stringLen:
        print("Interation: " + str(j))
        for stringIndex in range(stringLen):
            if currLine[j + stringIndex] != findString[stringIndex]:
                foundString = False
                break # don't keep searching if string isn't matching
        
        if foundString:
            printLine = True
            print("Index " + str(j) + " - " + str(j + stringLen -1) + ", ", end="")
            j += stringLen -1
        else:
            foundString = True
        j += 1

    if printLine:
        print(inputText[i])
        printLine = False

print()
     
