#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0  and i % 5:
            print('{}'.format(i),"FizzBuzz", end=" ")
        elif i % 3 == 0:
            print('{}'.format(i),"Fizz", end=" ")
        elif i % 5 == 0:
            print('{}'.format(i),"Buzz", end=" ")
        else:
            print(i, end=" ")
