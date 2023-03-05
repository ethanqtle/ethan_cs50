import sys
from pyfiglet import Figlet


def setFont(figlet):
    if len(sys.argv) == 3:
        optName, fontName = sys.argv[1:]
        invalidArg = optName not in ["-f", "--font"]
        if fontName not in figlet.getFonts():
            invalidArg = True
        if invalidArg:
            print("Invalid usage")
            sys.exit(1)
        figlet.setFont(font=fontName)


def renderInput(figlet):
    myStr = input("Input: ")
    print(figlet.renderText(myStr))


def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit(1)
    figlet = Figlet()
    setFont(figlet)
    renderInput(figlet)


if __name__ == "__main__":
    main()
