#!/usr/bin/python3
"""The function in this module carries out matrix multiplication
I wish I saw it in secondary school
"""


def matrix_mul(m_a, m_b):
    """This function carries out matrix multiplication of vectors?

    Args:
        m_a (list): Parameter 1
        m_b (list): Parameter 2

    Raises:
        TypeError: m_a must be a list
        TypeError: m_b must be a list
        TypeError: m_a must be a list of lists
        TypeError: m_b must be a list of lists
        ValueError: m_a can't be empty
        ValueError: m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size
        TypeError: each row of m_b must be of the same size
        ValueError: m_a and m_b can't be multiplied
    """
    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not (isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    if not all(isinstance(mem, list) for mem in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(mem, list) for mem in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for val in m_a:
        if not (all(isinstance(mem, int) for mem in val) or
                all(isinstance(mem, float) for mem in val)):
            raise TypeError("m_a should contain only integers or floats")
    for val in m_b:
        if not (all(isinstance(mem, int) for mem in val) or
                all(isinstance(mem, float) for mem in val)):
            raise TypeError("m_b should contain only integers or floats")
    for mem in m_a:
        if len(mem) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for mem in m_b:
        if len(mem) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for mem in m_a:
        temp = []
        for i in range(len(m_b[0])):
            a = 0
            for j in range(len(mem)):
                a += mem[j] * m_b[j][i]
            temp.append(a)
        result.append(temp)
    return result
