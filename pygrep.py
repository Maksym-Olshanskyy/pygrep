import sys
import time

# args
findString = ""
lineNumbers = False
tailLen = 0

#argument handling code
abort = False
i = 1
while i < len(sys.argv):
    match sys.argv[i]:
        case "-l":
            lineNumbers = True
        case "-t":
            i += 1
            if i < len(sys.argv):
                tailLen = int(sys.argv[i])
            else:
                print("pygrep: no quantity of lines given for -t, Aborting.")
                abort = True
        case _ :
            if sys.argv[i][0] == "-":
                print("pygrep: option " + sys.argv[i] + " is not recognized, Ignored.")
            elif findString == "":
                findString = sys.argv[i]
            else:
                print("pygrep: invalid input: " + sys.argv[i] + ", Ignored.")      
    i += 1

if findString == "":
    print("pygrep: no search string given, Aborting.")
    abort = True

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

        if printLine:
            print(inputText[i])
            printLine = False

else:
    print("pygrep -h for help")
