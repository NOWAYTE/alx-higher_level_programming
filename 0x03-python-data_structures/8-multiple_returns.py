#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        return (0, None)
    print(len(sentence))
    return sentence[0]
