#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = my_list.copy()
        for i in new_list:
            new_list[i] = True if new_list[i] % 2 == 0 else False
        return (new_list)
    return
