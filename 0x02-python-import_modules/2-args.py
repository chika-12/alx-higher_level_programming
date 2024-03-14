#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of arguments in a list"""
    import sys

    count = len(sys.argv) - 1
    if count == 1:
        print("1 argument:")
    elif count == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(count))

    for val in range(count):
        print("{}: {}".format(val + 1, sys.argv[val + 1]))
