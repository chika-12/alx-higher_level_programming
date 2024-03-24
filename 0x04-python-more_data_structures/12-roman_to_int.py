#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if roman_string == None:
        return None
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    add = 0
    index = len(roman_string)
    index2 = len(roman_string)
    char = 0
    if index2 < 2:
        add += d[roman_string]
    if index2 >= 2:
        while char < index - 1:
            if roman_string[char] in d:
                if d[roman_string[char]] >= d[roman_string[char + 1]]:
                    add += d[roman_string[char]]
                    if char == index - 2:
                        add += d[roman_string[-1]]
                if d[roman_string[char]] < d[roman_string[char + 1]]:
                    add += d[roman_string[char + 1]] - d[roman_string[char]]
                    char += 1
            char += 1
    return add
