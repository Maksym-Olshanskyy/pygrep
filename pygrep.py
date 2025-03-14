import sys
import time

# args
findString = ""
lineNumbers = False
tail = False
tailLen = 0

#argument handling code
abort = False
getHelp = False
i = 1
while i < len(sys.argv):
    match sys.argv[i]:
        case "-l":
            lineNumbers = True
        case "-t":
            tail = True
            i += 1
            if i < len(sys.argv):
                tailLen = int(sys.argv[i])
            else:
                print("pygrep: no quantity of lines given for -t, Aborting.")
                abort = True
                getHelp = True
        case "-h":
            print("Usage: [input text] | python pygrep [-h][-t num][-l] \"search string\"")
            print("  -h     : you are here!")
            print("  -l     : prints line numbers in front of each line")
            print("  -t num : tail, quantity of lines to print after a line with a match. ")
        case _ :
            if sys.argv[i][0] == "-":
                print("pygrep: option " + sys.argv[i] + " is not recognized, Ignored.")
                getHelp = True
            elif findString == "":
                findString = sys.argv[i]
            else:
                print("pygrep: invalid input: " + sys.argv[i] + ", Ignored.")
                getHelp = True
    i += 1

if findString == "":
    print("pygrep: no search string given, Aborting.")
    abort = True
    getHelp = True

if getHelp:
    print("pygrep -h for help")

if not abort:
    
    inputText = []
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


    #printArr()
    stringLen = len(findString)
    nonMatchLines = tailLen
    #print("Output is: ")
    # searching code
    for i in range(len(inputText)): # for each line in inputText
        currLine = inputText[i]
        
        foundString = True
        printLine = False

        #for j in range(): # for each char in line
        j = 0
        while j <= len(currLine) - stringLen:
            #print("Interation: " + str(j))
            for stringIndex in range(stringLen):
                if currLine[j + stringIndex] != findString[stringIndex]:
                    foundString = False
                    break # don't keep searching if string isn't matching
            if foundString:
                printLine = True
                print("Index " + str(j) + " - " + str(j + stringLen -1) + ", ", end="")
                j += stringLen -1 # jump over found string, because finding the string inside itself is impossible.
            else:
                foundString = True
            j += 1

        if printLine: # if there is an occurance, reset tail length
            nonMatchLines = 0
            print(inputText[i])
            printLine = False
        elif nonMatchLines < tailLen: # if tail length hasn't reached tailLen, keep printing lines
            nonMatchLines += 1
            print(inputText[i])
            printLine = False
