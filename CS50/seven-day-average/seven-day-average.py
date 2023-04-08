import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    previous_cases = {}
    new_cases = {}
    for row in reader:
        cases = row['cases']
        state = row['state']
        if row['state'] not in previous_cases:
            previous_cases[state] = list()
        previous_cases[state].append(cases)
        if len(previous_cases[state]) > 15:
            previous_cases[state] = previous_cases[state][1:]

    for state in list(previous_cases):
        for i in range(15):
            if state not in new_cases:
                new_cases[state] = list()
            new_cases[state].append(int(previous_cases[state][i]) - int(previous_cases[state][i-1]))
        new_cases[state] = new_cases[state][1:]
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        last_sum, sum, last_count, count = 0, 0, 0, 0
        for x in new_cases[state][0:7]:
            last_sum += x
            last_count += 1
            last_average = last_sum / last_count
        for x in new_cases[state][7:14]:
            sum += x
            count += 1
            average = sum / count
        try:
            change = (average - last_average) / last_average
            if change > 0:
                print(f"{state} had a 7-day average of {int(average)} and increase of {change:.2f}%")
            else:
                print(f"{state} had a 7-day average of {int(average)} and decrease of {abs(change):.2f}%")
        except ZeroDivisionError:
            print("average is 0")


main()
