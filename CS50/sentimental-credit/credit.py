# TODO
from cs50 import get_string
import re


def is_valid(number):
    l = len(number)
    total = 0
    times2 = False
    for i in range(l):
        n = int(number[l - 1 - i])
        if times2:
            if n * 2 < 10:
                total += 2 * n
            else:
                total += ((2 * n) % 10 + int((2 * n) / 10))
        else:
            total += n
        times2 = not times2
    if total % 10 == 0:
        return True
    return False


number = get_string("Number: ")

if len(re.findall('\d', number)) == len(number):

    if len(number) == 15 and (int(number[0:2]) == 34 or int(number[0:2]) == 37) and is_valid(number):
        print('AMEX')

    if len(number) == 16 and int(number[0:2]) in range(51, 56) and is_valid(number):
        print('MASTERCARD')

    if (len(number) == 13 or len(number) == 16) and int(number[0]) == 4 and is_valid(number):
        print('VISA')

    print('INVALID')

else:
    print('INVALID')
