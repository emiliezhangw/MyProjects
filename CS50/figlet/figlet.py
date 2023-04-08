import sys
from pyfiglet import Figlet
import random
figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(input("Input: ")))
    sys.exit(0)
elif len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))
        sys.exit(0)
print("Invalid usage")
sys.exit(1)
