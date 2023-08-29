#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        for i in range(x + 1):
            print(my_list[x])
except Exception as a:
    print(a)
