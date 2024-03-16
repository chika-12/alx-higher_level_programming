#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = ()
    if sentence:
        count = len(sentence)
        word = sentence[0]
    else:
        word = None
        count = len(sentence)
    new_tuple = (count, word,)
    return new_tuple
