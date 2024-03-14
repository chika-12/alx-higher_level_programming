#!/usr/bin/python3
import sys

argv = sys.argv
n = 1
print("{} arguments:".format(len(argv) - 1))
for val in argv:
    if val != argv[0]:
        print("{}: {}".format(n, val))
        n += 1
