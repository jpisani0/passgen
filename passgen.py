#!/usr/bin/env python3

# NAME: passgen.py
# AUTHOR: J. Pisani
# DATE: 9/4/24
#
# DESCRIPTION: main file for passgen

import sys
import argparse
import random

# Tuple for symbols to check if the user does not want symbols included in password
symbolsList = ("!", "\"", "#", "$", "%", "^", "*", "(", ")", "-", "+", "_", "=", "[", "{", "]", "}", "\\", "|", "",
               ",", "<", ".", ">", "`", "~", "/", "?", "@", "&", "\'", ":", ";")


# Check if a character is a symbol or not
def checkSymbol(character):
    for symbol in symbolsList:
        if symbol == character:
            return True

    return False


# Generate a random character for the cartoonpassword based on user settings
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


def main():
    parser = argparse.ArgumentParser(prog='passgen', description='simple CLI password generator', epilog='Example: passgen -l 25 -s --numbers --> generate a password that is 25 characters long and has no numbers or symbols')
    parser.add_argument('-l', '--length', type=int, nargs='?', default=20, help='length of the password to be generated')
    parser.add_argument('-s', '--symbols', type=bool, nargs='?', default=True, help='flag to not include symbols in the password')
    parser.add_argument('-n', '--numbers', type=bool, nargs='?', default=True, help='flag to not include numbers in the password')

    args = parser.parse_args()

    if args.length > 0:
        print("WARNING: your CLI has likely logged this password in plain text on your machine. Consider deleting it manually for maximum security")
        print(genPasswd(args.length, args.symbols, args.numbers))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
