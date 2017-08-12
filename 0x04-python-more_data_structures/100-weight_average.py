#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = list(map(lambda x: x[0] * x[1], my_list))
    value = list(map(lambda y: y[1], my_list))
    return sum(weight) / sum(value)
