import sys

# Check proper usage of command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

# Make sure the file is a Python file
try:
    count = 0

    # Open the Python file
    with open(sys.argv[1]) as file:
        # Read each line of the Python file
        for lines in file:
            # Count if the line is not a comment
            if not lines.lstrip().startswith("#") and not lines.isspace():
                count += 1
        # Print the lines of code
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
