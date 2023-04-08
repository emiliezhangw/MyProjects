# TODO
import re
from cs50 import get_string

text = get_string("Text: ")

letters = len(re.findall('[a-zA-Z]', text))
words = len(re.findall(' ', text)) + 1
sentences = len(re.findall('[?.!]', text))

l = letters / words * 100
s = sentences / words * 100
index = round(0.0588 * l - 0.296 * s - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print('Grade', index)