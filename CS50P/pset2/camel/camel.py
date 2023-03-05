import string

inputStr = input("camelCase: ")
print("snake_case: ", end="")
for c in inputStr:
    if c == c.upper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()
