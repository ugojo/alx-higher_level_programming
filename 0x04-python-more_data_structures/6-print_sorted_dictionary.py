#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = sorted(a_dictionary.keys())

    for key in ord_list:
        val = a_dictionary[key]
        print("{}: {}".format(key, val)
