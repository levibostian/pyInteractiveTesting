def infiniteLoopRemove(filName, searchStr):
    fil = open(filName, 'r+')

    outputStr = ""
    firstTime = True #first time seeing infinite loop

    for line in fil:
        if line.strip() == searchStr.strip():
            if firstTime:
                outputStr += line
                outputStr += "<<<<<<<<<< Infinite loop by user >>>>>>>>>>"
                firstTime = False
            else:
                continue
        else:
            outputStr += line

    fil.write("")
    fil.close()

    fil = open(filName, 'w')
    fil.write(outputStr)
    fil.close()

inputFil = input("Input file: ")
search = input("String to search for: ")
infiniteLoopRemove(inputFil, search)