# passgen

CLI Random Password Generator

# Using Passgen
## With Python3
Enter 'python3 passgen.py <options>' into your command line

## With Pyinstaller
The executable dist/passgen was compiled on my machine (Arch Linux), so you will obviously have to compile it yourself if you are on another operating system. I also recommend doing this even if you are on the same operating system as me, as I may have made changes but neglected to update the binary file.

1. Install Pyinstaller
   a. Install python and pip if you have not already
   b. Enter 'pip install pyinstaller' into your command line
2. While in the repository directory, enter 'pyinstaller --onefile passgen.py'
3. The binary file in dist/ will be overwritten and work on the machine you compiled it with

## Options
The manual can be accessed at anytime using the '-h' or '--help' option with passgen.

passgen: a simple CLI password generator

OPTIONS: \
  -l, --length: 
     Used to specify the desired length of the password. Any positive integer from 1 to 512. Default is 20 characters. \
  -s, --symbols: 
     Used to not include symbols in password. Symbols included by default. \
  -n, --numbers: 
     Used to not include numbers in password. Numbers enabled by default.

Example: passgen -l 25 -s --numbers --> generate a password that is 25 characters long and has no numbers or symbols
