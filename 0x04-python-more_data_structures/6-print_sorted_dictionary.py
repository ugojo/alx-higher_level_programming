#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = sorted(a_dictionary.keys())

    for i in ord_list:
        values = a_dictionary[i]
        print("{}:{}".format(i, values))
