#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as errmsg:
        print("Exception: {}".format(errmsg), file=sys.stderr)
        return False
    else:
        return True
