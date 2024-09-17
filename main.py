# NAME: main.py
# AUTHOR: J. Pisani
# DATE: 9/4/24
#
# DESCRIPTION: main file for passgen

import random

from options import *

# Global variables
length = 0 # Length of the password specified by the user
symbols = -1 # All symbols are included by default
symbolsSafe = -1 # Symbols that are "safe" for most software/accounts (excludes symbols that are typically disallowed)
numbers = -1 # Numbers are included in the password by default


# Generate a random character for the password based on user settings
def genCharacter():
    character = ""

    while character == "":
        character = chr(random.randint(33, 126))

        # If symbols are disabled
        if symbols == 0:
            if checkSymbol(character):
                character = ""
        # If numbers are disabled
        elif numbers == 0:
            if checkNumber(character):
                character = ""

    return character


# Generate the random password
def genPasswd():
    passwd = ""

    while len(passwd) < length + 1:
        passwd = passwd + genCharacter()

    return passwd


# TODO: put these user input lines into funcs and eventually have these options be command line options instead of asking at runtime
userInput = ""

# Get desired length of output, default is 20 characters
while length == 0:
    userInput = input("Enter desired length of password (default = 20): ")

    if userInput == "":
        length = 20
    # TODO: fix issue where program crashes when this input is not a number
    elif int(userInput) < 1 or int(userInput) > 512:
        print("Length outside of bounds, please choose a length between 1 and 512")
    else:
        length = int(userInput)

    print("")


while symbols == -1:
    userInput = input("Include symbols in password? (Y/n): ")

    if userInput == "Y" or userInput == "y" or userInput == "":
        symbols = 1
    elif userInput == "N" or userInput == "n":
        symbols = 0
    else:
        print("Invalid option")

    print("")


while numbers == -1:
    userInput = input("Include numbers in password? (Y/n): ")

    if userInput == "Y" or userInput == "y" or userInput == "":
        numbers = 1
    elif userInput == "N" or userInput == "n":
        numbers = 0
    else:
        print("Invalid option")

    print("")


print("WARNING: your CLI has likely logged this password in plain text on your machine. Consider manually deleting it from the log for maximum security.")
print(genPasswd())
