import random
def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def checkRange(val, lower, upper):
    return lower <= val and val <= upper

def get_level():
    while True:
        level = getInt("Level: ")
        if checkRange(level, 1, 3):
            return level

def generate_integer(level):
    if checkRange(level, 1, 3):
        match level:
            case 1:
                return random.randint(0, 9)
            case 2:
                return random.randint(10,99)
            case 3:
                return random.randint(100,999)
            case _:
                raise ValueError

def solveProblem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    for _ in range(3):
        sum = getInt(f"{x} + {y} = ")
        if sum != (x + y):
            print("EEE")
        else:
            return 1
    print(f"{x} + {y} =", x + y)
    return 0

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        score += solveProblem(level)
    print("Score: ", score)

if __name__ == "__main__":
    main()