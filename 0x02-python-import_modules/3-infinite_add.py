#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    import sys

    args = sys.argv
    result = 0
    if len(args) > 1:
        for i in range(1, len(args)):
            result += int(args[i])
        print(result)
    else:
        print("{}".format(result))
