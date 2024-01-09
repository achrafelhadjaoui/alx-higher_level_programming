#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) < 1:
        return len(sentence), None
    return len(sentence), sentence[0]
