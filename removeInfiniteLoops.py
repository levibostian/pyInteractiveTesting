def infiniteLoopRemove(searchStr):
    fil = open("output.txt", 'r+')

    outputStr = ""
    firstTime = True #first time seeing infinite loop

    for line in fil:
        if line.strip() == searchStr.strip():
            if firstTime:
                outputStr += line
                outputStr += "<<<<<<<<<< Infinite loop with above text >>>>>>>>>>"
                firstTime = False
            else:
                continue
        else:
            outputStr += line

    fil.write(outputStr)
    fil.close()

search = input("String to search for: ")
infiniteLoopRemove(search)