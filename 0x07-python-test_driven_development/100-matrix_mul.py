#!/usr/bin/python3
"""Matrix multiplication function"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(r, list) for r in m_a) or not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a cant be empty or m_b cant be empty")
    if not all(isinstance(e, (int , float) for r in m_a for element in r)) or not all(isinstance(e, (int , float) for r in m_b for e in r)):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if len(set(len(r) for r in m_a)) > 1 or len(set(len(r) for r in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0] != len(m_b):
        raise ValueError("m_a and m_b cant be multiplied")

    return [[sum(a * b for a , b in zip(r, c)) for c in zip(*m_b)] for r in m_a]
