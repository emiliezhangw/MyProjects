from datetime import date, timedelta
import sys
import re
import inflect


def main():
    today = date.today()
    try:
        birth = get_birth(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    print(get_minute(today, birth))


def get_birth(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        return date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
    else:
        raise ValueError


def get_minute(today, birth):
    t = today - birth
    delta = round(t.total_seconds() / 60)
    return f"{inflect.engine().number_to_words(delta, andword='').capitalize()} minutes"


if __name__ =="__main__":
    main()