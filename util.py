import os
import shutil

def renameAssignmentFiles():
    for files in os.listdir("assignments/"):
        if "_" in files:
            startIndex = files.find("_")
            endIndex = files.find("_", startIndex+1)
            fileName = files[startIndex+1:endIndex]

            shutil.move("assignments/"+files, "assignments/"+fileName+".py")