#!/usr/bin/python3
def islower(c):
    for alp in range(ord('a'), ord('z') + 1):
        if chr(alp) == c:
            return True
    return False
