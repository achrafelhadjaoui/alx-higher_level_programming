#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
res = number
if res < 0:
    res = number % -10
else:
    res = number % 10
if res > 5:
    print(f"Last digit of {number} is {res} and is greater than 5")
elif res < 6 and res != 0:
    print(f"Last digit of {number} is {res} and is less than 6")
else:
    print(f"Last digit of {number} is {res} and is 0")
