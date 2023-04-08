# TODO
from cs50 import get_float

while True:
    change = get_float("Change owed: ") * 100
    if change > 0:
        break

count = 0
if change >= 25:
    count += int(change / 25)
    change = change % 25

if change >= 10:
    count += int(change / 10)
    change = change % 10

if change >= 5:
    count += int(change / 5)
    change = change % 5

count += int(change)
print(count)

