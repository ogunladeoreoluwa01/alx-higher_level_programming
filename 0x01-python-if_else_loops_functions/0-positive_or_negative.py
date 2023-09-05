#!/usr/bin/python3
"""
This script generates a random signed number and prints whether it's positive, negative, or zero.
"""

import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive
if number > 0:
    # Print a message for a positive number
    print(f"{number} is positive")
elif number < 0:
    # Print a message for a negative number
    print(f"{number} is negative")
else:
    # Print a message for zero
    print(f"{number} is zero")
