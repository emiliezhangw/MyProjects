months = [
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
        "December"
    ]


def main():
    while True:
        date = input("Date: ").strip()
        if is_valid(date):
            break
    if (',') in date:
        day = date.split()[1][0]
        year = date.split()[2]
        month = months.index(date.split()[0]) + 1
    else:
        month, day, year = date.split('/')
    print(f"{int(year)}-{int(month):02}-{int(day):02}")


def is_valid(date):
    if '/' in date:
        for i in date.split('/'):
            if not i.isdigit():
                return False
        if 1 <= int(date.split('/')[0]) <= 12 and 1<= int(date.split('/')[1]) <= 31:
            return True
    elif ',' in date:
        day = date.split()[1].split(',')[0]
        year = date.split()[2]
        month = date.split()[0]
        if day.isdigit() and year.isdigit() and month in months and 1 <= int(day) <= 31:
            return True
    return False


if __name__ == "__main__":
    main()
