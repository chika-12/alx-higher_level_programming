#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    if not a_dictionary:
        return None
    else:
        new = a_dictionary[next(iter(a_dictionary))]
        if len(a_dictionary) < 2:
            first_key = next(iter(a_dictionary))
            return first_key
        for k, v in a_dictionary.items():
            if a_dictionary[k] > new:
                name = k
    return name
