#!/usr/bin/python3
for n in range(90):
    if(n % 10 > n / 10):
        if(n == 89):
            print("{:02d}".format(n))
        else:
            print("{:02d}".format(n), end=", ")
