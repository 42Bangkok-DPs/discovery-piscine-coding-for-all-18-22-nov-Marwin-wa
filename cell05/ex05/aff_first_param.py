#!/usr/bin/env python3

import sys

# Check if any parameters were passed to the script (excluding the script name)
if len(sys.argv) > 1:
    # Display the first parameter
    print(sys.argv[1])
else:
    # If no parameters are passed, print "none"
    print("none")
