#!/usr/bin/python3
'''Returns a tuple with length of string and its first character'''


def multiple_returns(sentence):

    if not sentence:
        print("{}", sentence, 'None')
    else:
        print("Length: {:d} - First character: {}".format(len(sentence), sentence[0]))
