#
/usr/bin/python3
"""a function that devides all elements of a matrix"""


def matric_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(i, (int, float)) for i in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix) for row in matrix):
            raise TypeError("Each row of the matric must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div = 0:
        raise ZeroDivisionError("division by zero")

    lis = []
    for row in matrix:
        for i in row:
            lis.append(i)


    return [[round (i / div, 2) for i in row] for row in matrix]

