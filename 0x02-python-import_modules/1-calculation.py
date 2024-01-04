#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

# Adds two integers
    a = 10
    b = 5
    addition = add(a, b)
print("{} + {} = {}".format(a, b, addition))

# Subtracts two integers
a = 10
b = 5
subtraction = sub(a, b)
print("{} - {} = {}".format(a, b, subtraction))

# Multiples two intergers
a = 10
b = 5
multiplication = mul(a, b)
print("{} * {} = {}".format(a, b, multiplication))

# Divides two integers
a = 10
b = 5
division = div(a, b)
print("{} / {} = {}".format(a, b, division))
