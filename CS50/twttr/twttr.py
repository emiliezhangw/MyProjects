def main():
    user_input = input("Input: ")
    print_omit_vowels(user_input)


def print_omit_vowels(s):
    for c in s:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            print(c, end='')
    print()


main()