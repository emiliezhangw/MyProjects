name = input("camelCase: ").strip()
for c in name:
    if c.isupper():
        name = name.split(c, 1)[0] + '_' + c.lower() + name.split(c, 1)[1]
print("snake_case: " + name)
