names = []

#prompt user for names
while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

#print names
print("Adieu, adieu, to ", end='')
if len(names) < 2:
    print(names[0])
elif len(names) < 3:
    print(f"{names[0]} and {names[1]}")
else:
    for name in names[:-1]:
        print(name, end=', ')
    print(f"and {names[-1]}")



