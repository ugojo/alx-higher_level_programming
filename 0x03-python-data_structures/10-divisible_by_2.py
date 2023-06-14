#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = []
    length = len(my_list)
    for i in range(length):
        if(my_list[i] % 2 == 0):
            return multiple.append(True)
        else:
            return multiple.append(False)
    return(multiple)
