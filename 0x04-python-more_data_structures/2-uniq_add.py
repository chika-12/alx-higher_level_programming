#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        num = 0
        for val in set(my_list):
            num += val
    return num
