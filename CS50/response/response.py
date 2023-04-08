import validators
#from validator_collection import validators, checkers

#if checkers.is_email(input("What's your email address? ")):
    #print("Valid")
#else:
    #print("Invalid")

if validators.email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")