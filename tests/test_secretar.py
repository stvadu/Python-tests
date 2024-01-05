from unittest import TestCase
from secretar import get_name, get_directory, add


class TestSolution(TestCase):
    def test_10006(self):
        x = '10006'
        res = get_name(x)
        expected = 'Аристарх Павлов'
        self.assertEqual(res, expected)

    def test_11_2(self):
        x = '11-2'
        res = get_directory(x)
        expected = '1'
        self.assertEqual(res, expected)

    def test_101(self):
        x = '101'
        res = get_name(x)
        expected = 'Документ не найден'
        self.assertEqual(res, expected)

    def test_add(self):
        res = add('international passport', '311 020203', 'Александр Пушкин', '3')
        self.assertTrue(res)

    def test_311_020203_directory(self):
        # add('international passport', '311 020203', 'Александр Пушкин', '3')
        x = '311 020203'
        res = get_directory(x)
        expected = '3'
        self.assertEqual(res, expected)

    def test_311_020203_name(self):
        # add('international passport', '311 020203', 'Александр Пушкин', '3')
        x = '311 020203'
        res = get_name(x)
        expected = 'Александр Пушкин'
        self.assertEqual(res, expected)

    def test_311_020204_directory(self):
        x = '311 020204'
        res = get_directory(x)
        expected = 'Полки с таким документом не найдено'
        self.assertEqual(res, expected)
