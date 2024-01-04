#!/usr/bin/python3
import sys
argument = sys.argv
argLength = len(argument)

if (argLength == 0):
    print("{} {}{}".format(argLength - 1, "arguments", "."))
elif (argLength == 1):
    print("{} {}{}".format(argLength - 1, "arguments", ":"))
else:
    print("{} {}{}".format(argLength - 1, "arguments", ":"))

for a in range(1, argLength):
    print("{}{} {}".format(a, ":", argument[a]))
