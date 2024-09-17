# NAME: options.py
# AUTHOR: J. Pisani
# DATE: 9/16/24
#
# DESCRIPTION: contains functions for checking options specified by the user when calling this program

# Tuple for "safe" symbols to be used in password generation. These are symbols that SHOULD be accepted by most if they restrict certain symbols
symbolsList = ("!", "\"", "#", "$", "%", "^", "*", "(", ")", "-", "+", "_", "=", "[", "{", "]", "}", "\\", "|", "",
               ",", "<", ".", ">", "`", "~", "/", "?", "@", "&")


# Check if a character is a symbol or not
def checkSymbol(character):
    for symbol in symbolsList:
        if symbol == character:
            return True

    return False


# Check if a character is a number or not
def checkNumber(character):
    for num in range(0, 10):
        if str(num) == character:
            return True

    return False