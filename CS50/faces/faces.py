
def main():
    answer = input()
    print(convert(answer))


def convert(to):
    return to.replace(":)", "🙂").replace(":(", "🙁")


main()
