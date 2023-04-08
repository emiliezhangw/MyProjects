def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and s[0:2].isalpha() and 2 <= len(s) <= 6:
        for c in s:
            # make sure the first number not equal to 0
            if c.isdigit():
                if c == '0':
                    return False
                else:
                    s = s.split(c, 1)[1]
                    # make sure there is no alpha characters after the first number
                    for char in s:
                        if char.isalpha():
                            return False
                    return True
        return True
    return False


if __name__ == "__main__":
    main()
