import sys
import csv, tabulate


def main():
    checkSysArgv()
    table = readCsvFile(sys.argv[1])
    print(tabulate.tabulate(table, headers="firstrow", tablefmt="grid"))


def readCsvFile(fileName):
    try:
        table = []
        with open(fileName) as csvFile:
            csvRead = csv.reader(csvFile)
            for row in csvRead:
                table.append(row)
        return table
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


def checkSysArgv():
    numArg = len(sys.argv) - 1
    if numArg == 0:
        print("Too few command-line arguments")
        sys.exit(1)
    elif numArg == 1:
        if fileExt(sys.argv[1]) != ".csv":
            print("Not a csv file")
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
