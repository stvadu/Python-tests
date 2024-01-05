from unittest import TestCase
from vote import vote

class TestSolution(TestCase):
    def test_1_1_1_2_3_numbers(self):
        a = 1
        b = 1
        c = 1
        d = 2
        e = 3
        res = vote([a, b, c, d, e])
        expected = 1
        self.assertEqual(res, expected)

    def test_1_2_3_2_2_numbers(self):
        a = 1
        b = 2
        c = 3
        d = 2
        e = 2
        res = vote([a, b, c, d, e])
        expected = 2
        self.assertEqual(res, expected)

