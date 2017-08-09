#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    # iter tokenizes elemetns in string
    a = iter(tuple_a)
    b = iter(tuple_b)
    for index in range(2):  # next gets next token else return 0 if none found
        result.append(next(a, 0) + next(b, 0))
    return (tuple(result))
