#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = str(number)[-1]
d = int(last_digit)

if d == 0:
    print(f"Last digit of {number} is {d} and is 0")
elif d > 6:
    print(f"Last digit of {number} is {d} and is greater than 5")
else:
    print(f"Last digit of {number} is {d} and is less than 6 and not 0")
