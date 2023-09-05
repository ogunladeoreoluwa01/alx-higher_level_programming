#!/usr/bin/python3
"""
This script generates a random signed number and prints whether it's positive, negative, or zero.
"""
import random
# Generate a random number between -10 and 10
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
