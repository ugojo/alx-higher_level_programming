#!/usr/bin/python3
for n in range(100):
    if(n <=9):
        print("0{}".format(n), end=", ")
    elif(n == 99):
        print("{}".format(n))
    else:
        print("{}".format(n), end=", ")
