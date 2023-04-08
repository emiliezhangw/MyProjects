from random import randint

def main():
    n = get_positive_int("Level: ")
    i = randint(1, n)
    while True:
        x = get_positive_int("Guess: ")
        if x < i:
            print("Too small!")
        elif x > i:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_int(prompt):
    while True:
        try:
            i = int(input(prompt))
            if i > 0:
                return i
        except ValueError:
            pass


if __name__ == "__main__":
    main()