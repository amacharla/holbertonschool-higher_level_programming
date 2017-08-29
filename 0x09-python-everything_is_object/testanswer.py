""" Testing Answers
>>> import testanswer
>>> a = 89
>>> b = 100
>>> print(a == b) # 2
False

>>> a = 89
>>> b = 89
>>> print(a == b) # 3
True

>>> a = 89
>>> b = a
>>> print(a is b) # 4
True

>>> a = 89
>>> b = a + 1
>>> print(a is b) # 5
False

>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2) # 6
True

>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2) # 7
True

>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2) # 8
True

>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2) # 9
True

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2) # 10
True

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2) # 11
False

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2) # 12
True

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2) # 13
True

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2) # 14
[1, 2, 3, 4]

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2) # 15
[1, 2, 3]

>>> def increment(n):
...     n += 1
>>>
>>> a = 1
>>> increment(a)
>>> print(a) # 16
1

>>> def increment(n):
...     n.append(4)
>>>
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l) # 17
[1, 2, 3, 4]

>>> def assign_value(n, v):
...     n = v
>>>
>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> assign_value(l1, l2)
>>> print(l1) # 18
[1, 2, 3]

>>> copy_list = __import__('19-copy_list').copy_list
>>>
>>> my_list = [1, 2, 3]
>>> print(my_list) # 19.1
[1, 2, 3]
>>>
>>> new_list = copy_list(my_list)
>>>
>>> print(my_list) # 19.2
[1, 2, 3]
>>> print(new_list) # 19.3
[1, 2, 3]
>>>
>>> print(new_list == my_list) # 19.4
True
>>> print(new_list is my_list) # 19.5
False

>>> a = ()
>>> type(a) is tuple # 20
True

>>> a = (1, 2)
>>> type(a) is tuple # 21
True

>>> a = (1)
>>> type(a) is tuple # 22
False

>>> a = (1, )
>>> type(a) is tuple # 23
True

>>> a = (1)
>>> b = (1)
>>> a is b # 24
True

>>> a = (1, 2)
>>> b = (1, 2)
>>> a is b # 25
False

>>> a = ()
>>> b = ()
>>> a is b # 26
True

>>> a = [1, 2, 3, 4]
>>> a_before = id(a)
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> a_after = id(a)
>>> a_before == a_after # 27
False

>>> a = [1, 2, 3]
>>> a_before = id(a)
>>> a += [4]
>>> a_after = id(a)
>>> a_before == a_after # 28
True

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
