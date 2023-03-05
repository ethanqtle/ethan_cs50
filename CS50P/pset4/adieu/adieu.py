import inflect
def getNames():
    nameList = []
    while True:
        try:
            nameList.append(input("Name: "))
        except EOFError:
            return nameList


def main():
    p = inflect.engine()
    names = getNames()
    print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()