#!/usr/bin/python3
"""This module also odoes matrix multiplication, but with two lines of code
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """It uses numpy to carry out matrix multiplication

    Args:
        m_a (list): a matrix of integers or floats
        m_b (list): a matrix of integers or floats

    Returns:
        list: the multiplied result
    """
    return (np.matmul(m_a, m_b))
