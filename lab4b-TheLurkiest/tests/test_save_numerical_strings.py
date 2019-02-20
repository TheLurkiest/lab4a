"""
test_save_numerical_strings.py
Mihaela
February 5, 2019; Updated Feb 20, 2019
"""

import unittest
from lab4problems.problems import Problems


class TestSaveNumericalStrings(unittest.TestCase):
    """ ..."""
    def setUp(self):
        self.p = Problems()

    def test_one_num_in_list_of_two(self):
        """ ..."""
        actual_result = self.p.save_numerical_strings(['hi', '20'])
        expected_result = ['20']
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
