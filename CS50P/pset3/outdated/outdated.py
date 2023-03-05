MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def dateFormat1(dateStr):
    fields = dateStr.split("/")
    if len(fields) != 3:
        return ""
    try:
        for i in range(len(fields)):
            fields[i] = int(fields[i])
    except ValueError:
        return ""

    mon, day, year = fields

    if mon < 1 or 12 < mon:
        return ""
    if day < 1 or 31 < day:
        return ""

    return "%04d-%02d-%02d" % (year, mon, day)


def dateFormat2(dateStr):
    fields = dateStr.split()
    if len(fields) != 3:
        return ""
    monName, day, year = fields
    if monName in MONTHS:
        mon = MONTHS.index(monName) + 1
    else:
        return ""

    if day[-1] != ",":
        return ""

    try:
        # skip last ","
        day = int(day[:-1])
        year = int(year)

        if day < 1 or 31 < day:
            return ""
        return "%04d-%02d-%02d" % (year, mon, day)
    except ValueError:
        return ""


def main():
    while True:
        dateStr = input("Date: ")
        newDate = dateFormat1(dateStr)
        if newDate != "":
            print(newDate)
            break
        newDate = dateFormat2(dateStr)
        if newDate != "":
            print(newDate)
            break


if __name__ == "__main__":
    main()
