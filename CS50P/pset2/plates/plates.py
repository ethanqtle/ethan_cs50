def first2Letter(s):
    if len(s) < 2:
        return False
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


def validAlphaNumLen(s):
    if not (2 <= len(s) and len(s) <= 6):
        return False
    for c in s:
        if not c.isalnum():
            return False
    return True


def alphaThenDigit(s):
    alphaCount = 0
    digitCount = 0
    searchAlpha = True
    for c in s:
        if searchAlpha:
            if c.isalpha():
                alphaCount += 1
            else:
                if c == "0":
                    return False
                searchAlpha = False
        else:
            if not c.isdigit():
                return False
            else:
                digitCount += 1
    return True


def is_valid(s):
    return first2Letter(s) and validAlphaNumLen(s) and alphaThenDigit(s)


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
