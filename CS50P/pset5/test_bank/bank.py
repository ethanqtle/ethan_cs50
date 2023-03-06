
def main():
    greeting = input("Greeting: ")
    payAmount = value(greeting)
    print(f"${payAmount}")

def value(greeting):
    cleanGreeting = greeting.strip().lower()
    if cleanGreeting.find("hello") == 0:
        return 0
    elif cleanGreeting.find("h") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()