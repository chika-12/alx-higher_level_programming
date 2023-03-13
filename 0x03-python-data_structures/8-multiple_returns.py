#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
        for i in sentence:
            length += 1
    return(length, first_char)

            
