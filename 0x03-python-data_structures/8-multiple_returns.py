#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == ""):
        sentence[0] = "None"
    print(len(sentence))
    return sentence[0]
