import sys
import os
import time

def ReadFromStdin():
    saveArr = []
    while True:
            try:
                saveArr.append(input())
            except EOFError:
                # no more information
                break
    return saveArr

def ReadFromFile(fileName):
    saveArr = []
    with open(fileName, newline='') as file:
        for line in file:
            saveArr.append(line.rstrip("\n"))
    return saveArr

# args
findString = ""
lineNumbers = False
tail = False
tailLen = 0
readFile = False
fileName = ""
color = True

#argument handling code
abort = False
getHelp = False
i = 1
while i < len(sys.argv):
    match sys.argv[i]:
        case "-l":
            lineNumbers = True
        case "-t":
            i += 1
            if i < len(sys.argv):
                tail = True
                tailLen = int(sys.argv[i])
            else:
                print("pygrep: no quantity of lines given for -t, Aborting.")
                abort = True
                getHelp = True
        case "-i":
            i += 1
            if i < len(sys.argv): # check if file path is given
                readFile = True
                fileName = sys.argv[i]
                if not os.path.exists(fileName): # check if file exists
                    print("pygrep: input file doesn't exist, Aborting.")
                    abort = True
                elif not os.access(fileName, os.R_OK): # check if file is readable 
                    print("pygrep: input file permission denied, Aborting.")
                    abort = True
            else:
                print("pygrep: no input file name given, Aborting.")
                abort = True
                getHelp = True
            # after all this code is done, and abort flag is off, should be safe to read file
            # without try/catch
        case "-c":
            color = False
        case "-h":
            print("\033[1;31mUsage: [input text] | python pygrep [-h][-t num][-l] \"search string\" \033[0m")
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

    if readFile:
        inputText = ReadFromFile(fileName)
    else:
        inputText = ReadFromStdin()

    stringLen = len(findString)
    printLines = tailLen +1
    #print("Output is: ")
    # searching code
    for i in range(len(inputText)): # for each line in inputText
        currLine = inputText[i]
        indexes = []
        
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
                printLines = 0
                indexes.append(j) # starting index
                j += stringLen -1 # jump over found string, because finding the string inside itself is impossible.
            else:
                foundString = True
            j += 1

        if printLines <= tailLen: # if tail length hasn't reached above tailLen, keep printing lines
            if color:
                k = len(indexes) -1
                while k >= 0:
                    currLine = currLine[:indexes[k] + stringLen] + "\033[0m" + currLine[indexes[k] + stringLen:] # reset color
                    currLine = currLine[:indexes[k]] + "\033[1;31m" + currLine[indexes[k]:] # set color
                    k -= 1
            if lineNumbers:
                currLine = "Line " + str(i +1) + ": " + currLine 
            printLines += 1
            print(currLine)