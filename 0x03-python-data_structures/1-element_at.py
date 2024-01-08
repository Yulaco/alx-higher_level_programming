#!/usr/bin/python3

# Function gets an element from a list

def element_at(my_list, idx):
    if idx <= 0:
        print("{}".format(None))
    elif idx >= len(my_list):
        print("{}".format(None))
    else:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
