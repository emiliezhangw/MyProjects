
grocery = {}

while True:
    try:
        item = input().strip()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except EOFError:
        break

for k in sorted(grocery):
    print(grocery[k], k.upper())





