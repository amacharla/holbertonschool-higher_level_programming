#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and search and replace:
        return (list(map(lambda num: replace if num == search else num, my_list)))
    return
