import sys
import csv

# Make sure the proper usage of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too many comman-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        last, first = student["name"].split(", ")
        house = student["house"]
        writer.writerow({"first": first, "last": last, "house": house})


