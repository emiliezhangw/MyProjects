def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    new_word = ""
    for c in word:
        if c not in ['a', 'e', 'i', 'o', 'u']:
            new_word += f"{c}"
    return new_word


if __name__ == "__main__":
    main()