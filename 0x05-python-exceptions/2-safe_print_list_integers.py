#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end="")
                count += 1
        print()
        return (count)
    except (ValueError, TypeError, IndexError):
        print()
    return (count)
