def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x = int(fraction.split('/')[0])
            y = int(fraction.split('/')[1])
            z = round(x / y * 100)
            if x > y:
                raise ValueError
            return z
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
