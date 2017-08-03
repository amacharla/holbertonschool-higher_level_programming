#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for num in argv[1:]:
        result += int(num)
    print(result)
