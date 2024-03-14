#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of arguments in a list"""
    import sys

    argv = sys.argv
    n = 1
    if len(argv) - 1 == 1:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    for val in argv:
        if val != argv[0]:
            print("{}: {}".format(n, val))
            n += 1
