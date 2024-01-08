#!/usr/bin/python3

# Function gets an element from a list

def element_at(my_list, idx):
    if (idx < 0):
        print('None')
    elif (idx >= len(my_list)):
        print('None')
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))
