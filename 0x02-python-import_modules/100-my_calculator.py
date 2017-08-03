#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = int(argv[1]), argv[2], int(argv[3])
    operators = ['+', '-', '*', '/']
    func = [add, sub, mul, div]

    for index, sign in enumerate(operators):
        if op == sign:
            result = func[index](a, b)
            break
    if op != sign:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, op, b, result))
