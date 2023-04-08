answer = input("Greeting: ").strip()
if answer[0:5].lower() == "hello":
    print("$0")
elif answer[0].lower() == 'h':
    print("$20")
else:
    print("$100")
