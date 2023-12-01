#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 1:
        if len(args) > 2:
            print("{} arguments:".format(len(args) - 1))
        else:
            print("{} argument:".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))
    else:
        print("{} arguments.".format(0))
