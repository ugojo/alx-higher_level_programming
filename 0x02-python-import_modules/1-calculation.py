#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    a = 10
    b = 5
    sums = add(a, b)
    print("{} + {} = {}".format(a, b, sums))
    subt =  sub(a, b)
    print("{} - {} = {}".format(a, b, subt))
    multi = mul(a, b)
    print("{} * {} = {}".format(a, b, multi))
    divi = div(a, b)
    print("{} / {} = {}".format(a, b, divi))
