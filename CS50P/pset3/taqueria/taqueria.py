MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def readItem():
    items = input("Item: ").split()
    for i in range(len(items)):
        items[i] = items[i].capitalize()
    return " ".join(items)


def main():
    total = 0.0
    while True:
        try:
            menuItem = readItem()
        except EOFError:
            print()
            break
        else:
            if menuItem in MENU:
                total += MENU[menuItem]
                print("Total: $%0.2f" % (total))


if __name__ == "__main__":
    main()
