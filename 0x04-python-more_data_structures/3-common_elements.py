#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        result = []
        for a in set_1:
            for b in set_2:
                if a == b:
                    result.append(a)
        return result
    return
