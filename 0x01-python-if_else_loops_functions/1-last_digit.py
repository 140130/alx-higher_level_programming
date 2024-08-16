#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
mod = number % 10
mod = number % -10
if mod > 5:
    print("Last digit of {:d} and {:d} is greater than 5".format(number, mod))
elif mod == 0:
    print("Last digit of {:d}  and {:d} is 0".format(number, mod))
else:
    print("Last digit of {:d}  and {:d} is  less than 6 and not 0".format(number, mod))
