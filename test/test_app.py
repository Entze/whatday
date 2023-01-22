import unittest

from whatday.app import get_century_drift


class TestGetCenturyDrift(unittest.TestCase):
    def test_eighteenth_century(self):
        for year in range(1700, 1800):
            with self.subTest(year=year):
                expected = 0
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)

    def test_nineteenth_century(self):
        for year in range(1800, 1900):
            with self.subTest(year=year):
                expected = 5
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)

    def test_twentieth_century(self):
        for year in range(1900, 2000):
            with self.subTest(year=year):
                expected = 3
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)

    def test_twenty_first_century(self):
        for year in range(2000, 2100):
            with self.subTest(year=year):
                expected = 2
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)

    def test_twenty_second_century(self):
        for year in range(2100, 2200):
            with self.subTest(year=year):
                expected = 0
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)

    def test_twenty_third_century(self):
        for year in range(2200, 2300):
            with self.subTest(year=year):
                expected = 5
                actual, _ = get_century_drift(year)
                self.assertEqual(expected, actual)
