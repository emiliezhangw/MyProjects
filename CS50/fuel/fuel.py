def main():
    fuel = get_fraction("Fraction: ")
    if fuel >= 99:
        print('F')
    elif fuel <= 1:
        print('E')
    else:
        print(f"{fuel}%")


def get_fraction(prompt):
    while True:
        try:
            s = input(prompt).strip()
            x = int(s.split('/')[0])
            y = int(s.split('/')[1])
            if x <= y:
                return x
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
