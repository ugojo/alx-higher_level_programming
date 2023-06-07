#!/usr/bin/python3
for ch in range(97, 123):
    if("{:c}".format(ch) not in ('q', 'e')):
        print("{:c}".format(ch), end="")
