#!/usr/bin/python3
for alp in range(ord('z'), ord('a') - 1, - 1):
    if alp % 2 == 1:
        alp = alp - 32
        print("{}".format(chr(alp)), end="")
    else:
        print("{}".format(chr(alp)), end="")
