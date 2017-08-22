#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(args[0], args[1])
    except Exception as error:  # gets execption from function fct()
        print("Exception: {}".format(error), file=sys.stderr)
    finally:
        return result
