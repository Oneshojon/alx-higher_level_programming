#!/usr/bin/python3
# 2-args.py

import sys
args = sys.argv
if len(args) > 1:
    print("{} arguments:".format(len(args) - 1))
    for i in range(1, len(args)):
         print("{}: {}".format(i, args[i]))
else:
    print("{} arguments.".format(0))
