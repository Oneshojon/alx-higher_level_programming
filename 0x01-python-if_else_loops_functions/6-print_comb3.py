#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and j :
            print("{:d}".format(i), end="")
            if i == 8 and j == 9:
                print("{}".format(j))
            else:
                print("{:d}, ".format(j), end="")
