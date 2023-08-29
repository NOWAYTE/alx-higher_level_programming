#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end="")
            count += 1

    except IndexError as a:
        print(f"{a}: list index is out of range")
    print()

    return count

