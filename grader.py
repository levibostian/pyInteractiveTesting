"""
File: grader.py
code: Levi Bostian - bostianl@uni.edu
Description: Script to iterate through all students programs, tests programs with certain input, 
             and sends output to output file for easy grading. 
"""

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
                results += "### Run "+str(runsCount)+"###\n"
                results += runTests(fil.name, inputSet)
                results += "\n\n"
                runsCount += 1
            
            if results == None:
                output += "None"
            else: 
                output += results
    output = checkForInfiniteLoops(output)
    writeResultsToFile(output)

def checkForInfiniteLoops(outStr):
    lineCountOccur = 0
    prevLine = ""
    searchStrs = []

    for line in outStr:
        if line == prevLine:
            lineCountOccur += 1
            if lineCountOccur > 10 and not (line in searchStrs):
                searchStrs.append(line)
        else:
            lineCountOccur = 0
        prevLine = line

    for items in searchStrs:
        outStr = util.infiniteLoopRemove(outStr, items)

    return outStr

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
    except IOError:
        if input("input.txt file missing. Generate one?: (y/n): ").lower() == "y":
            generateInputFil()
        sys.exit()
    inputFil.close()

def generateInputFil():
    newInputFil = open('input.txt', 'w')
    fileStr = "# grader input.txt\n"+ \
        "# Enter one value per line per input() statement to send to student's assignment."
    newInputFil.write(fileStr)
    newInputFil.close()

def getStudentName(fil):
    return "--- Student Last Name: "+fil.name.split('/')[1][:-3].title()+" ---" #return last name

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