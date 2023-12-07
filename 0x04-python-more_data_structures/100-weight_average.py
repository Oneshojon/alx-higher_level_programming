#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight_mass = sum(score * weight for score, weight in my_list)
    weight_sum = sum(weight for i, weight in my_list)
    result = weight_mass / weight_sum
    return (result)
