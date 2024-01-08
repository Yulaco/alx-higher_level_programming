#!//usr/bin/python3
'''Replaces an element in a list at a specific position
without modifiying the original list'''


def new_in_list(my_list, idx, element):
    new_list = my_list

    if (idx <= 0):
        print("{}".format(my_list))
    elif (idx <= len(my_list)):
        print("{}".format(my_list))
    else:
        print("{}".format(new_list[idx]))

    for new_list in range(my_list):
        print("{}".format(new_list[idx]))
