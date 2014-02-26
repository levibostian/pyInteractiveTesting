import os
import shutil

def renameAssignmentFiles():
    for files in os.listdir("assignments/"):
        if "_" in files and files.endswith(".py"):
            startIndex = files.find("_")
            endIndex = files.find("_", startIndex+1)
            fileName = files[startIndex+1:endIndex]

            shutil.move("assignments/"+files, "assignments/"+fileName+".py")


def infiniteLoopRemove(outputStr, searchStr):
    out = ""
    firstTime = True #first time seeing infinite loop

    for line in outputStr:
        if line.strip() == searchStr.strip():
            if firstTime:
                out += line
                out += "<<<<<<<<<< Infinite loop by user >>>>>>>>>>"
                firstTime = False
            else:
                continue
        else:
            out += line

    return out