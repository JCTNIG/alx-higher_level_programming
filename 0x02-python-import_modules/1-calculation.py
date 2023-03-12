#!/usr/bin/python3
if __name__ == " __main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = :d{}".format(int(a, b, add(a + b))))
    print("{:d} - {:d} = {:d}".format(int(a, b, sub(a - b))))
    print("{:d} * {:d} = {:d}".format(int(a, b, mul(a * b))))
    print("{:d} / {:d} = {:d}".format(int(a, b, div(a / b))))
