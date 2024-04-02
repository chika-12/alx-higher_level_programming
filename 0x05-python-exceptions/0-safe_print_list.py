#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for num in range(x):
            print(f"{my_list[num]}", end="")
            count += 1
    except Exception:
        pass
    print()
    return count
