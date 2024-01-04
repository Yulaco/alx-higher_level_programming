#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv
    argLength = len(argument)

if (argLength == 1):
    print("{} {}{}".format(argLength - 1, "arguments", ":"))
elif (argLength == 2):
    print("{} {}{}".format(argLength - 1, "argument", ":"))
else:
    print("{} {}{}".format(argLength - 1, "arguments", "."))

for a in range(1, argLength):
    print("{}{} {}".format(a, ":", argument[a]))
