from unittest import TestCase, expectedFailure
from yandex_folder import make_yandex_dir
import requests

class TestSolution(TestCase):
    @expectedFailure
    def test_OK(self):
        res = make_yandex_dir()
        expected = 201
        self.assertEqual(res, expected)

    @expectedFailure
    def test_no_token(self):
        res = make_yandex_dir()
        expected = 401
        self.assertEqual(res, expected)

    @expectedFailure
    def test_dir_already_exists(self):
        res = make_yandex_dir()
        expected = 409
        self.assertEqual(res, expected)

