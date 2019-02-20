"""
test_triple_nums.py
Mihaela
January 29, 2019; Updated Feb 20, 2019
"""

import unittest
from lab4problems.problems import Problems


class TestTripleNums(unittest.TestCase):
    """ ..."""
    def setUp(self):
        self.p = Problems()

    def test_three_nums(self):
        """ ..."""
        actual_result = self.p.triple_nums([1, 2, 3])
        expected_result = [1, 6, 9]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
