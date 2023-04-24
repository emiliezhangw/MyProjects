import sys
import re
import inflect
from pyfiglet import Figlet
from tabulate import tabulate
from datetime import date, timedelta


convert = [
    {'time': ['1. 12-hour to 24-hour', '2. calculate time from a date to another', '3. calculate a future or past date']},
    {'temperature': ['1. Fahrenheit to Degree Celsius', '2. Degree Celsius to Fahrenheit']},
    {'length': ['1. Foot to Inch', '2. Inch to Foot', '3. Mile to Meter', '4. Meter to Mile', '5. Centimeter to Inch', '6. Inch to Centimeter']},
    {'weight': ['1. Pound to Ounce', '2. Ounce to Pound', '3. Ounce to Gram', '4. Gram to Ounce', '5. Gram to Pound', '6. Pound to Gram']},
    ]

def main():
    # Welcome message to user
    print("I'm your conversion helper", "This is a list of conversions, that I can do for you: ", sep=" 🧁🧁 ")

    while True:
        try:
            # Describe the options for user
            for i in range(4):
                print(f"{i + 1}. {list(convert[i])[0]}");

            # Prompt user for option
            option = get_option("Which area would you want to choose? ", 4)

            # Prompt user for specific needs
            analyze(option)
            print()
        except ValueError:
            pass
        except EOFError:
            break

    # Print farewell message to user
    figlet = Figlet()
    figlet.setFont(font="contessa")
    print(figlet.renderText("Bye!"))


#  Prompt user for option
def get_option(s, n):
    while True:
        try:
            i = int(input(s))
            if i in range(1, n + 1):
                return i
            else:
                raise ValueError
        except ValueError:
            pass


# Prompt user for specific needs
def analyze(choose):
    print(f"\nThank you for choosing {list(convert[choose - 1])[0]} conversion", "I can do a lot of things!", sep=" 🧁🧁 ")

    # Show the table of options
    print(tabulate(convert[choose - 1], headers="keys", tablefmt="grid", colalign=("left",)))

    # Get the number of choose from atop dictionary
    num_of_choose = len(convert[choose - 1][list(convert[choose - 1])[0]])

    # Prompt user for option
    option = get_option("What do you want me to do for you today? ", num_of_choose)

    match(choose):
        case 1:
            print(time_convert(option))
        case 2:
            if option == 1:
                while True:
                    try:
                        print(fahrenheit_to_celsius(input("Hi! Please give me a Fahrenheit temperature! ").strip()))
                        break
                    except ValueError:
                        pass
            else:
                while True:
                    try:
                        print(celsius_to_fahrenheit(input("Hi! Please give me a Celsius temperature! ").strip()))
                        break
                    except ValueError:
                        pass

        case 3:
            while True:
                try:
                    print(length_convert(option, input("Hi! please give me a number of length: ").strip()))
                    break
                except ValueError:
                    pass

        case 4:
            while True:
                try:
                    print(weight_convert(option, input("Hi! please give me a number of weight: ").strip()))
                    break
                except ValueError:
                    pass
        case _ :
            return


def time_convert(option):
    # Make sure what the user want to do within time conversion
    match(option):
        case 1:
            while True:
                try:
                    print("Hi! please give me a time you would like to convert!\nThe format should be like '9:00 AM to 5:00 PM' or '9 AM to 5 PM'")
                    time_before = input().strip()
                    time_after = time_hour_clock(time_before)
                    return f"The 24-hour clock of {time_before} is:\n{time_after}"
                except ValueError:
                    pass

        case 2:
            while True:
                try:
                    print("Hi! please give me a begin date and end date\nThe format should be like 'YYYY-MM-DD to YYYY-MM-DD' or 'YYYY-MM-DD to today' or 'today to YYYY-MM-DD'! ")
                    time_begin, time_end = input().strip().split(' to ')
                    t = time_pass_by(time_begin.lower(), time_end.lower())
                    delta = round(t.total_seconds() / 60)
                    return f"The period from {time_begin} to {time_end} is:\n{inflect.engine().number_to_words(delta, andword='').capitalize()} minutes!"
                except ValueError:
                    pass

        case 3:
            while True:
                try:
                    print("Hi! Please give me a date\nThe format of date should be like 'YYYY-MM-DD' or 'today'! ".strip())
                    dates = input()
                    day = int(input("Great! Please give the number of days from this date "))
                    if dates.lower() == 'today':
                        time_new = date.today() + timedelta(days=day)
                        return f"The date {day} days from {date.today()} is: {time_new}"
                    elif matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", date):
                        time_new = date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3))) + timedelta(days=day)
                        return f"The date {day} days from {date.today()} is: {time_new}"
                except ValueError:
                    pass

        case _:
            return


def time_hour_clock(s):
    # Make sure user input correct formats
    if matches := re.search(r"^(\d+)(?::(\d+))?(?:\s)?(AM|PM)(?:\s)?to(?:\s)?(\d+)(?::(\d+))?(?:\s)?(AM|PM)$", s, re.IGNORECASE):

        # Make sure the time is valid
        if 0 <=int(matches.group(1)) <= 12 and 0 <=int(matches.group(4)) <= 12:
            if matches.group(3).upper() == "AM":
                if int(matches.group(1)) == 12:
                    hour1 = 0
                else:
                    hour1 = int(matches.group(1))
            else:
                if int(matches.group(1)) == 12:
                    hour1 = 12
                else:
                    hour1 = int(matches.group(1)) + 12
            if matches.group(6).upper() == "AM":
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


def time_pass_by(begin, end):
    if match1 := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", begin):
        if match2 := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", end):
            return date(int(match2.group(1)), int(match2.group(2)), int(match2.group(3))) - date(int(match1.group(1)), int(match1.group(2)), int(match1.group(3)))
        elif end == 'today':
            return date.today() - date(int(match1.group(1)), int(match1.group(2)), int(match1.group(3)))
    elif begin == 'today':
        if match2 := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", end):
            return date(int(match2.group(1)), int(match2.group(2)), int(match2.group(3))) - date.today()
        elif end == 'today':
            return date.today() - date.today()
    raise ValueError


def temperate_convert(o):
    match(o):
        case 1:
            while True:
                try:
                    return fahrenheit_to_celsius(input("Hi! Please give me a Fahrenheit temperature! ").strip())
                except ValueError:
                    pass
                except EOFError:
                    break

        case 2:
            while True:
                try:
                    return celsius_to_fahrenheit(input("Hi! Please give me a Celsius temperature! ").strip())
                except ValueError:
                    pass
                except EOFError:
                    break
        case _:
            return


def fahrenheit_to_celsius(s):
    f_tmp = float(s)
    c_tmp = (f_tmp - 32) * 5 / 9
    return f"{f_tmp:.2f} degrees in Fahrenheit is {c_tmp:.2f} degrees in Celsius"


def celsius_to_fahrenheit(s):
    c_tmp = float(s)
    f_tmp = c_tmp * 9 / 5 + 32
    return f"{c_tmp:.2f} degrees in Celsius is {f_tmp:.2f} degrees in Fahrenheit"


def length_convert(i, s):
    length_convert = [
        {'from': 'Feet', 'to': 'Inches', 'value': 12},
        {'from': 'Inches', 'to': 'Feet', 'value': 1/12},
        {'from': 'Miles', 'to': 'Meters', 'value': 1609.344},
        {'from': 'Meters', 'to': 'Miles', 'value': 1/1609.344},
        {'from': 'Centimeters', 'to': 'Inches', 'value': 1/2.54},
        {'from': 'Inches', 'to': 'Centimeters', 'value': 2.54},
        ]
    l_begin = float(s)
    l_after = length_convert[i - 1]['value'] * l_begin
    return f"{l_begin:.2f} {length_convert[i - 1]['from'].lower()} is {l_after:.2f} {length_convert[i - 1]['to'].lower()}"


def weight_convert(i, s):
    weight_convert = [
        {'from': 'Pound', 'to': 'Ounce', 'value': 16},
        {'from': 'Ounce', 'to': 'Pound', 'value': 1/16},
        {'from': 'Ounce', 'to': 'Gram', 'value': 28.3495},
        {'from': 'Gram', 'to': 'Ounce', 'value': 1/28.3495},
        {'from': 'Gram', 'to': 'Pound', 'value': 1/453.592},
        {'from': 'Pound', 'to': 'Gram', 'value': 453.592},
        ]
    w_begin = float(s)
    w_after = weight_convert[i - 1]['value'] * w_begin
    return f"{w_begin:.2f} {weight_convert[i - 1]['from'].lower()}s is {w_after:.2f} {weight_convert[i - 1]['to'].lower()}s"


if __name__ == "__main__":
    main()