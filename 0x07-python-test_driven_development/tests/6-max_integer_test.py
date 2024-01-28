#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Thi test is for testing the max_integer function

    Args:
        unittest (int): It tests the function, max_integer which returns
        the highest integer in a list
    """
    def test_result(self):
        """Tests for the max when there's only one max value
        """
        self.assertEqual(max_integer([1, 4, 5, 7, 3]), 7)

    def test_two_maximum_numbers(self):
        """Tests when there are two maximum numbers
        """
        self.assertEqual(max_integer([1, 5, 2, 6, 7, 6, 7]), 7)

    def test_no_member_in_list(self):
        """Tests when the list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_ints_and_floats(self):
        """Test a combination of integers and floats
        """
        self.assertEqual(max_integer([3, 4.5, 5.6, 2, 6.5, 3.4]), 6.5)

    def test_only_one_member(self):
        """Test only one number in the list
        """
        self.assertEqual(max_integer([5]), 5)

    def test_a_character(self):
        """Test a character in the string
        """
        self.assertEqual(max_integer("r"), "r")

    def test_string(self):
        """test a string
        """
        self.assertEqual(max_integer("hello"), "o")

    def test_an_empty_string(self):
        """Test an empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test a list of strings
        """
        self.assertEqual(max_integer(["hello", "my", "be", "is"]), "my")

    def test_matrix(self):
        """Test a matrix
        """
        self.assertEqual(max_integer([[4, 3], [2, 6], [3, 5]]), [4, 3])
