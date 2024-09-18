# NAME: main.py
# AUTHOR: J. Pisani
# DATE: 9/4/24
#
# DESCRIPTION: main file for passgen

import random
import sys

from options import *
from userInput import getOptions


# Generate a random character for the password based on user settings
def genCharacter():
    character = ""

    while character == "":
        character = chr(random.randint(33, 126))

        # If symbols are disabled
        if not symbols:
            if checkSymbol(character):
                character = ""

        # If numbers are disabled
        if not numbers:
            if checkNumber(character):
                character = ""

    return character


# Generate the random password
def genPasswd():
    passwd = ""

    while len(passwd) < length:
        passwd = passwd + genCharacter()

    return passwd


length, symbols, numbers = getOptions(sys.argv)

print("WARNING: your CLI has likely logged this password in plain text on your machine. Consider manually deleting it from the log for maximum security.")
print(genPasswd())
