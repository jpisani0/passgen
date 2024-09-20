# NAME: generatePassword.py
# AUTHOR: J. Pisani
# DATE: 9/17/24
#
# DESCRIPTION: contains functions for randomly generating the password

import random

from options import *


# Generate a random character for the password based on user settings
def genCharacter(symbols, numbers):
    character = ""

    while character == "":
        character = chr(random.randint(33, 126))

        # If symbols are disabled
        if not symbols:
            if checkSymbol(character):
                character = ""

        # If numbers are disabled
        if not numbers:
            if character.isdigit():
                character = ""

    return character


# Generate the random password
def genPasswd(length, symbols, numbers):
    passwd = ""

    while len(passwd) < length:
        passwd = passwd + genCharacter(symbols, numbers)

    return passwd
