import sys
import csv
from tabulate import tabulate

if len(sys.argv)  < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    table = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        #reader = csv.reader(file)
        for row in reader:
            table.append(row)
        headers="keys"
        #headers="firstrow"
        print(tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
