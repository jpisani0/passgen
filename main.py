# NAME: main.py
# AUTHOR: J. Pisani
# DATE: 9/4/24
#
# DESCRIPTION: main file for passgen

import sys

from userInput import getOptions
from generatePassword import genPasswd


length, symbols, numbers = getOptions(sys.argv)

# Check that length is not -1, indicating an error with the user inputted options
if length != -1:
    print("passgen(): WARNING: your CLI has likely logged this password in plain text on your machine. Consider manually deleting it from the log for maximum security.")
    print(genPasswd(length, symbols, numbers))

