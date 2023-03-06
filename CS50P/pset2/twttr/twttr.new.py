
def main():
    text = input("Input: ")
    print("Output:", shorten(text))

def shorten(word):
    vowels = "AEIOUaeiou"
    new_text = ""
    for letter in word:
        if letter not in vowels:
            new_text += letter
    return new_text

if __name__ == "__main__":
    main()