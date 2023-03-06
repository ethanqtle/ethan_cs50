def readFraction():
    while True:
        try:
            myStr = input("Fraction: ")
            items = myStr.split("/")
            frac = int(items[0]) / int(items[1])
            if 0 <= frac and frac <= 1.0:
                return frac
        except (ValueError, ZeroDivisionError):
            pass


def printFraction(fraction):
    percent = fraction * 100.0
    if percent <= 1.0:
        print("E")
    elif percent < 99.0:
        print("%0.0f%%" % (percent))
    else:
        print("F")


def main():
    printFraction(readFraction())


if __name__ == "__main__":
    main()
