#!/usr/bin/python3
for alph in range(ord('z') , ord('a') - 1, - 1):
    if alph % 2 == 0:
        diff = 0
    else:
        diff = 32

    print("{}".format(chr(alph - diff)), end="")
