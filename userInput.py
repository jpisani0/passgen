# NAME: userInput.py
# AUTHOR: J. Pisani
# DATE: 9/17/24
#
# DESCRIPTION: contains functions for handling user input

# Help/manual printout
def printHelp(errorMsg):
    if errorMsg != "":
        print(errorMsg+"\n")

    print("passgen: a simple CLI password generator\n")
    print("OPTIONS:")
    print("  -l, --length")
    print("     Used to specify the desired length of the password. Any positive integer from 1 to 512. Default is 20 characters.")
    print("  -s, --symbols")
    print("     Used to not include symbols in password. Symbols included by default.")
    print("  -n, --numbers")
    print("     Used to not include numbers in password. Numbers enabled by default.\n")
    print("Example: passgen -l 25 -s --numbers --> generate a password that is 25 characters long and has no numbers or symbols")


# Get the length of the password from user input
def getLength(userInput):
    if userInput < 1 or userInput > 512:
        printHelp("Invalid length, please choose an integer between 1 and 512")
        return -1
    else:
        return userInput


# Get the options from user input
def getOptions(options):
    length = 20  # Default length is 20
    symbols = True  # Symbols enabled by default
    numbers = True  # Numbers enabled by default
    index = 1

    if len(options) != 0:
        # Loop through the maximum amount of options
        while index < len(options):
            if options[index] == "-h" or options[index] == "--help":
                printHelp("")
                length = -1
                break
            elif options[index] == "-l" or options[index] == "--length":
                # Check that the entered length is an integer
                if options[index + 1].isdigit():
                    length = getLength(int(options[index + 1]))
                    index += 1
                else:
                    printHelp("Invalid length")
                    length = -1
                    break
            elif options[index] == "-s" or options[index] == "--symbols":
                symbols = False
            elif options[index] == "-n" or options[index] == "--numbers":
                numbers = False
            else:
                printHelp("Invalid option")
                length = -1
                break

            index += 1

    return length, symbols, numbers
