# NAME: main.py
# AUTHOR: J. Pisani
# DATE: 9/4/24
#
# DESCRIPTION: main file for passgen

import random

# Global variables
length = 0 # Length of the password specified by the user
symbols = -1 # All symbols are included by default
symbolsSafe = -1 # Symbols that are "safe" for most software/accounts (excludes symbols that are typically disallowed)
numbers = -1 # Numbers are included in the password by default
asciiStart = 0 # Start of valid ascii characters for password generation
asciiEnd = 0 # End of valid ascii characters for password generation

# Tuple for "safe" symbols to be used in password generation. These are symbols that SHOULD be accepted by most if they restrict certain symbols
safeSymbolsList = ("!", "#", "$", "%", "$")

# # Generate a random character for the password based on user settings
# def genCharacter():


# Generate the random password
def genPasswd():
    passwd = ""
    asciiCode = 0
    currentCharacter = ""
    lastCharacter = ""

    while len(passwd) < length:
        # TODO: add functionality to change generation of passwd based on user options, prob in func called genCharacter()
        # genCharacter()
        asciiCode = random.randint(33, 126)
        currentCharacter = chr(asciiCode)

        # REVIEW: is it necessary to restrict using the same character twice in a row? maybe a different number
        # Do not use the same character as before
        if currentCharacter == lastCharacter:
            continue

        passwd = passwd + currentCharacter

    return passwd


# TODO: put these user input lines into funcs and eventually have these options be command line options instead of asking at runtime
userInput = ""

# Get desired length of output, default is 20 characters
while length == 0:
    userInput = input("Enter desired length of password (default= 20): ")

    if userInput == "":
        length = 20
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


if symbols == 1:
    while symbolsSafe == -1:
        userInput = input("Use safe symbols only? (y/N): ")

        if userInput == "Y" or userInput == "y":
            symbolsSafe = 1
        elif userInput == "N" or userInput == "n" or userInput == "":
            symbolsSafe = 0
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
