import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'^<iframe(?: width="\d+" height="\d+")? src="https?://(?:www.)?youtube\.com/embed/(\w+)"(?: title=".+" frameborder="\d+" allow=".+; .+; .+; .+; .+; .+" .+)?></iframe>',
        s,
    ):
        return f"https://youtu.be/{matches.group(1)}"
    return None


if __name__ == "__main__":
    main()
