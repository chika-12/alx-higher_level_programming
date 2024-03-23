#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    if not a_dictionary:
        return None
    else:
        new = a_dictionary[next(iter(a_dictionary))]
        for k, v in a_dictionary.items():
            if a_dictionary[k] > new:
                name = k
    return name
