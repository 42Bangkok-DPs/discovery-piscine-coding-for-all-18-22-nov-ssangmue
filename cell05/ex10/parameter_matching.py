#!/usr/bin/env python3
import sys

# Check the number of command-line arguments
if len(sys.argv) != 2:
    print("none")
else:
    # Ask the user for a word
    user_input = input("Enter a word: ")

    # Compare the user input with the command-line argument
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

