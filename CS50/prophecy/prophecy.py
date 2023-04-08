import csv
from cs50 import SQL

#open students.db using sqlite
db = SQL("sqlite:///students.db")

# Open CSV file
with open("students.csv", "r") as file:
    # Create DictReader
    reader = csv.DictReader(file)
    for row in reader:
        id = row['id']
        name = row['student_name']
        house = row['house']
        head = row['head']
        db.execute("INSERT OR REPLACE INTO students(id, student_name) VALUES(?, ?)", id, name)
        db.execute("INSERT OR REPLACE INTO houses(name, house) VALUES(?, ?)", name, house)
        db.execute("INSERT OR REPLACE INTO house_assignments(house, head) VALUES(?, ?)", house, head)
