#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    num = []
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    for i in my_list:
        del my_list[idx]
        if i != my_list[idx]:
            num.append(my_list[i])
    return (my_list)
