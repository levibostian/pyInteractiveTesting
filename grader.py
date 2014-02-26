import os
import pexpect 
import sys
import util # util.py
import time

def main():
    util.renameAssignmentFiles()

    clearOutput()
    checkInputFileExists()

    inputList = processInput()

    output = getOutputHeader()
    assignmentNames = os.listdir("assignments/")
    assignmentNames.sort()
    for fil in assignmentNames:
        if fil.endswith(".py"):
            fil = open("assignments/"+fil, "r")
            results = ""

            output += getStudentName(fil)+"\n"

            runsCount = 1
            for inputSet in inputList:
                results += "### Run "+str(runsCount)+" ###\n"
                results += runTests(fil.name, inputSet)
                results += "\n\n"
                runsCount += 1
            
            if results is None:
                output += "None"
            else: 
                output += results

    writeResultsToFile(output)

def clearOutput():
    outputFil = open("output.txt", 'w')
    outputFil.write("")
    outputFil.close()

def processInput():
    inputSetsList = []
    inputFil = open("input.txt", 'r')

    inputSet = []
    for line in inputFil:
        line = line.strip()
        if line.startswith('#'):
            continue
        elif line == "" or line == " ":
            if len(inputSet) > 0:
                inputSetsList.append(inputSet)
                inputSet = []
        else:
            inputSet.append(line)

    if len(inputSet) > 0:
        inputSetsList.append(inputSet)
    
    return inputSetsList

def getOutputHeader():
    return "File: output.txt\n" + \
           "Description: stdout from grader.py\n" + \
           "Date: "+time.strftime("%c")+"\n\n"

def writeResultsToFile(output):
    outputFil = open("output.txt", 'w')
    outputFil.write(output)
    outputFil.close()

def checkInputFileExists():
    try:
        inputFil = open('input.txt', 'r')
        inputFil.close()
    except IOError:
        generateInputFil()
        print("input.txt file missing. New file generated.")
        print("Please edit input file and try again.")
        sys.exit()

def generateInputFil():
    newInputFil = open('input.txt', 'w')
    fileStr = \
        "# tester input.txt\n"+ \
        "# lines beginning with # are comments.\n"+ \
        "# Enter one value per line per input() statement to send to script.\n"+ \
        "# Separate sets of input statements with a blank line.\n"
    newInputFil.write(fileStr)
    newInputFil.close()

def getStudentName(fil):
    return "--- File name: "+fil.name.split('/')[1][:-3].title()+" ---"

def runTests(filName, inSet):
    child = pexpect.spawn("python3 "+filName)
    time.sleep(.5) #needs sleep to allow print() to go to console

    for item in inSet:
        child.sendline(item)

    try:
        child.expect(pexpect.EOF, timeout=1)
        child.close()
    except:
        return child.before.decode(encoding='UTF-8') # Translate byte to string. Need for Python 3.
    return child.before.decode(encoding='UTF-8') # Translate byte to string. Need for Python 3.

main()