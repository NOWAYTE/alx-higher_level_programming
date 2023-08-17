#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
quot_result = divide(a, b)
print("The sum of {} and {} is: {}".format(a, b, sum_result))
print("The difference between {} and {} is: {}".format(a, b, diff_result))
print("The product of {} and {} is: {}".format(a, b, prod_result))
print("The quotient of {} divided by {} is: {}".format(a, b, quot_result))
