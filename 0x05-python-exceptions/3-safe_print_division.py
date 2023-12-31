#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        try:
            print("Inside result: {}".format(result))
            return (result)
        except NameError:
            print("Inside result: None")
