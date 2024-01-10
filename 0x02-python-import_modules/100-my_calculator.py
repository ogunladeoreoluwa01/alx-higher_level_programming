#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys as s
    if len(s.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        s.exit(1)
    c = s.argv[2]
    if c == "+" or c == "-" or c == "*" or c == "/":
        pass
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        s.exit(1)
    a = int(s.argv[1])
    b = int(s.argv[3])
    if s.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif s.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif s.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif s.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    s.exit(0)
