def main():
    timeInput = input("What time is it? ")
    mealHour = convert(timeInput)

    if 7 <= mealHour and mealHour <= 8:
        print("breakfast time")
    elif 12 <= mealHour and mealHour <= 13:
        print("lunch time")
    elif 18 <= mealHour and mealHour <= 19:
        print("dinner time")


def convert(timeStr):
    hour, minute = timeStr.split(":")
    return int(hour) + int(minute) / 60


if __name__ == "__main__":
    main()
