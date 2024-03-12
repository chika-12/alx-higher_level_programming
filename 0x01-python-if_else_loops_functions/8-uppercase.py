#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for alp in str:
        if ord(alp) >= 97 and ord(alp) <= 122:
            new_str += chr(ord(alp) - 32)
        else:
            new_str += alp
    print("{}".format(new_str))
