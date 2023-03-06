def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
    """
    convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
    and returns that fraction as a percentage rounded to the nearest int between 0 and 100,
    inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert
    should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
    """
    items = fraction.split("/")
    x = int(items[0])
    y = int(items[1])
    percent = round(x / y * 100.0)
    if 0 <= percent and percent <= 100:
        return percent
    else:
        raise ValueError


def gauge(percentage):
    """
    gauge expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int
    """
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"

if __name__ == "__main__":
    main()
