#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.

def safe_print_division(a, b):

    try:
        divide = a / b
    except (ZeroDivisionError, TypeError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
