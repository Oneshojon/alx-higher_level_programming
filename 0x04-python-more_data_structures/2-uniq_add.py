#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        my_list = []
    new = list(set(my_list))
    result = 0
    for i in new:
        result += i
    return result
