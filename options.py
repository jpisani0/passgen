# NAME: options.py
# AUTHOR: J. Pisani
# DATE: 9/16/24
#
# DESCRIPTION: contains functions for checking options specified by the user when calling this program

# Tuple for symbols to check if the user does not want symbols included in password
symbolsList = ("!", "\"", "#", "$", "%", "^", "*", "(", ")", "-", "+", "_", "=", "[", "{", "]", "}", "\\", "|", "",
               ",", "<", ".", ">", "`", "~", "/", "?", "@", "&", "\'", ":", ";")


# Check if a character is a symbol or not
def checkSymbol(character):
    for symbol in symbolsList:
        if symbol == character:
            return True

    return False
