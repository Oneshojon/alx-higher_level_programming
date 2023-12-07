#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    skeys = sorted(list(a_dictionary))
    for i in skeys:
        print("{}: {}".format(i, a_dictionary[i]))
    
