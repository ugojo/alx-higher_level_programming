#!/usr/bin/python3
def number_keys(a_dictionary):
    num_keys = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num_keys += 1
    return(num_keys)
