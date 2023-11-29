#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("{:2d}, ".format(i), end="")
        i += 1
else:
    print("99")
