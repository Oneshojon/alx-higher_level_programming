#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    import calculator_1
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(args) == 4 and args[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        operator = args[2]
        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, a + b))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, a - b))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, a * b))
        else:
            print("{} {} {} = {}".format(a, operator, b, a / b))
