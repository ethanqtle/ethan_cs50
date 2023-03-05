def printList(groceryList):
    items = list(groceryList.keys())
    items = sorted(items)
    print()
    for item in items:
        print("%0d %s" % (groceryList[item], item))


def main():
    groceryList = {}
    while True:
        try:
            item = input()
        except EOFError:
            printList(groceryList)
            break
        else:
            item = item.upper()
            if item in groceryList:
                groceryList[item] += 1
            else:
                groceryList[item] = 1


if __name__ == "__main__":
    main()
