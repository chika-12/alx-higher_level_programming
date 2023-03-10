#!/usr/bin/python3
if __name__ == "__main__":
    """prints infinite additional computation"""

    import sys
    add = 0
    count = len(sys.argv)
    for i in range(1, count):
        add += int(sys.argv[i])
    print("{:d}".format(add))
