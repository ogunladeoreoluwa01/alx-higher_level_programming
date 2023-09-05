#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    end = -num % 10
    end = -end
else:
    end = num % 10
if end > 5:
    print(f"Last digit of {num} is {end} and is greater than 5")
elif end < 6 and end != 0:
    print(f"Last digit of {num} is {end} and is less than 6 and not 0")
elif end == 0:
    print(f"Last digit of {num} is {end} and is 0")
