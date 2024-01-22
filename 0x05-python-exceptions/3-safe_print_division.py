#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError

        result = a / b
        return result

    except (ValueError, ZeroDivisionError):
        result = None
        return None

    finally:
        print("Inside result: {}".format(result))
