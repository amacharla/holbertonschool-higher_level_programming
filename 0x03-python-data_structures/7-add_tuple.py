#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        result = []
        for i in range(2):
            a1 = tuple_a[i] if len(tuple_b) == 2 else 0
            a2 = tuple_b[i] if len(tuple_b) == 2 else 0
            result.append(a1 + a2)
        return (tuple(result))
    return
