#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    i = dir(hidden_4)
    for n in i:
        if n[:2] != "__":
            print(n)
