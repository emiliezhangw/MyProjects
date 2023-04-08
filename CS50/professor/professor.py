import random


def main():
    # Prompt user for level
    n = get_level()
    # initial the number of score
    score = 0

    # Generate ten math problems
    for _ in range(10):
        # generate x and y
        x = generate_integer(n)
        y = generate_integer(n)
        # initial the number of tries
        count = 0
        while True:
            try:
                # After three wrong tries, print the right answer of the problem
                if count > 2:
                    print(f"{x} + {y} = {x + y}")
                    break

                # Prompt user for the answer of x + y
                answer = int(input(f"{x} + {y} = "))

                # Decide whether the answer is right
                if answer == x + y:
                    score += 1
                    break

                # print 'EEE' if the answer if wrong
                print("EEE")
                count += 1

            # print 'EEE' if catch a ValueError
            except ValueError:
                print("EEE")
                count += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            i = int(input("Level: "))
            if i - 1 in range(3):
                return i
        except ValueError:
            pass


def generate_integer(level):
    # Decide the range of random numbers
    high = pow(10, level) - 1
    if level != 1:
        low = pow(10, level - 1)
    else:
        low = 0
    print(high, low)
    # Return random number between the given range
    return random.randint(low, high)


if __name__ == "__main__":
    main()
