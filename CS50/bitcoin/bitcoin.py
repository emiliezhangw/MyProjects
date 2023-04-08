import sys
import json
import requests

# Make sure user input only one command line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    # Make sure the command line argument is a float number
    i = float(sys.argv[1])
    # Queries the API for the CoinDesk Bitcoin Price Index and get a JSON objext
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Get the value of key rate_float in the dict
    n = response.json()["bpi"]["USD"]["rate_float"]
    # Print the cost with four decimal places and using ',' as a thousands separator
    print(f"${n * i:,.4f}")

# Catch exceptions and exit with an error message
except ValueError:
    sys.exit("Command-line argument is not a number")

# Catch exceptions and exit
except requests.RequestException:
    sys.exit()
