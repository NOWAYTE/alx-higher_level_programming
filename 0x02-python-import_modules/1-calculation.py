#!/usr/bin/python3
if __name__ == "__main__":
    import calculator*
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.fomrat(a, b, div(a, b)))
