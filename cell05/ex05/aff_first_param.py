#!/usr/bin/env python3
import sys

# Check if there are any parameters passed
if len(sys.argv) < 2:
    print("none")
else:
    # Print the first parameter (excluding the script name)
    print(sys.argv[1])
