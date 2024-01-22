#!/usr/bin/python3
# Prints the first x elements of a list and only integers.

def safe_print_list_integers(my_list=[], x=0):

    item = 0
    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num], end=""))
            item = item + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (item)
