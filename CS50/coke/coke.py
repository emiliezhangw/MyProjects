amount = 50
while True:
    x = int(input("Insert Coin: "))
    if x not in [25, 10, 5]:
        print("Amount Due:", abs(amount))
        continue
    else:
        amount -= x
    if amount <= 0:
        print("Change Owed:", abs(amount))
        break
    print("Amount Due:", amount)
