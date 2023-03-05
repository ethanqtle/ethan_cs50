import random
def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def main():
    while True:
        level = getInt("Level: ")
        if level >= 1:
            break
    secret = random.randint(1, level)
    while True:
        guess = getInt("Guess: ")
        if 1 <= guess <= level:
            if guess > secret:
                print("Too large!")
            elif guess < secret:
                print("Too small!")
            else:
                print("Just right!")
                break


if __name__ == "__main__":
    main()