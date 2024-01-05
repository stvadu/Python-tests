from unittest import TestCase
from discriminant import discriminant, solution

class TestSolution(TestCase):
    def test_1_8_15_numbers(self):
        x = 1
        y = 8
        z = 15
        res = solution(x, y, z)
        expected = (-3.0, -5.0)
        self.assertEqual(res, expected)

    def test_1__13_12_numbers(self):
        x = 1
        y = -13
        z = 12
        res = solution(x, y, z)
        expected = (12.0, 1.0)
        self.assertEqual(res, expected)

    def test__4_28__49_numbers(self):
        x = -4
        y = 28
        z = -49
        res = solution(x, y, z)
        expected = 3.5
        self.assertEqual(res, expected)

    def test_1_1_1_numbers(self):
        x = 1
        y = 1
        z = 1
        res = solution(x, y, z)
        expected = 'корней нет'
        self.assertEqual(res, expected)
