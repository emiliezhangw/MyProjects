import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Make sure user input correct formats
    if matches := re.search(r"^(\d+)(?::(\d+))? (AM|PM) to (\d+)(?::(\d+))? (AM|PM)$", s):

        # Make sure the time is valid
        if 0 <=int(matches.group(1)) <= 12 and 0 <=int(matches.group(4)) <= 12:
            if matches.group(3) == "AM":
                if int(matches.group(1)) == 12:
                    hour1 = 0
                else:
                    hour1 = int(matches.group(1))
            else:
                if int(matches.group(1)) == 12:
                    hour1 = 12
                else:
                    hour1 = int(matches.group(1)) + 12
            if matches.group(6) == "AM":
                if int(matches.group(4)) == 12:
                    hour2 = 0
                else:
                    hour2 = int(matches.group(4))
            else:
                if int(matches.group(4)) == 12:
                    hour2 = 12
                else:
                    hour2 = int(matches.group(4)) + 12

            # Decide which formats the user choose
            if not (matches.group(2) or matches.group(5)):
                return f"{hour1:02}:00 to {hour2:02}:00"
            if 0 <=int(matches.group(2)) <= 59 and 0 <=int(matches.group(5)) <= 59:
                minute1 = int(matches.group(2))
                minute2 = int(matches.group(5))
                return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    raise ValueError


if __name__ == "__main__":
    main()