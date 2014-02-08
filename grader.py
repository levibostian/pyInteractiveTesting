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

    checkInputFileExists()

    output = getOutputHeader()
    for fil in os.listdir("assignments/"):
        if fil.endswith(".py"):
            fil = open("assignments/"+fil, "r")

            output += getStudentName(fil)+"\n"

            results = runTests(fil.name)
            
            if results == None:
                output += "None\n\n"
            else: 
                output += results+"\n\n"
    writeResultsToFile(output)

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

def runTests(filName):
    child = pexpect.spawn("python3 "+filName)

    inputFil = open("input.txt", 'r')
    for line in inputFil:
        if not line.startswith("#"):
            child.sendline(line.strip())
    inputFil.close()

    try:
        # child.expect(pexpect.EOF, timeout=1)
        child.expect(pexpect.EOF, timeout=2)
        child.close()
    except:
        return child.before.decode(encoding='UTF-8') # Translate byte to string. Need for Python 3.
    return child.before.decode(encoding='UTF-8') # Translate byte to string. Need for Python 3.

main()