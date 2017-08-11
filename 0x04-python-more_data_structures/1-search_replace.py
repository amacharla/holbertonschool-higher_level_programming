#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and len(my_list) != 0:
        return (list(map(lambda num: replace if num == search else num, my_list)))
    return
