#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        max_num = my_list[0]
        count = len(my_list)

        for num in range(count):
            if my_list[num] > max_num:
                max_num = my_list[num]
    else:
        return None
    return max_num
