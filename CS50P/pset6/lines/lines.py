import sys
def main():
    checkSysArgv()
    lineCount = countPySourceLine(sys.argv[1])
    print(lineCount)


def countPySourceLine(fileName):
    try:
        lineCount = 0
        with open(fileName) as myFile:
            for line in myFile:
                cleanLine = removeComment(line)
                if cleanLine != "":
                    lineCount += 1
        return lineCount
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


def removeComment(line):
    line = line.strip()
    if "#" in line:
        line = line[:line.index("#")]
    return line

def checkSysArgv():
    numArg = len(sys.argv) - 1
    if numArg == 0:
        print("Too few command-line arguments")
        sys.exit(1)
    elif numArg == 1:
        if fileExt(sys.argv[1]) != ".py":
            print("Not a Python file")
            sys.exit(1)
    else:
        print("Too many command-line arguments")
        sys.exit(1)


def fileExt(fileName):
    fileName = fileName.strip().lower()
    if fileName.rfind(".") >= 0:
        return fileName[fileName.rfind(".") :]
    else:
        return ""


if __name__ == "__main__":
    main()