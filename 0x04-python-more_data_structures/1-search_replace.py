#!/usr/bin/python3
def search_replace(my_list, search, replace):
    num = list(map(lambda val: val if val != search else replace, my_list))
    return num
