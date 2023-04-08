import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
