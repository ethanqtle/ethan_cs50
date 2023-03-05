userStr = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)
cleanList = userStr.lower().split()
cleanStr = " ".join(cleanList)
if cleanStr == "42" or cleanStr == "forty-two" or cleanStr == "forty two":
    print("Yes")
else:
    print("No")
