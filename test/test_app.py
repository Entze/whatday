import datetime
import unittest

from whatday.app import get_century_drift, calculate_weekday


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


class TestCalculateWeekday(unittest.TestCase):
    def test_same_as_strftime_seventeenth_century(self):
        for year in range(1600, 1700):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_eighteenth_century(self):
        for year in range(1700, 1800):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_nineteenth_century(self):
        for year in range(1800, 1900):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_twentieth_century(self):
        for year in range(1900, 2000):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_twenty_first_century(self):
        for year in range(2000, 2100):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_twenty_second_century(self):
        for year in range(2100, 2200):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)

    def test_same_as_strftime_twenty_third_century(self):
        for year in range(2200, 2300):
            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        datetime.date(year, month, day)
                    except ValueError:
                        continue
                    with self.subTest(year=year, month=month, day=day):
                        expected = datetime.date(year, month, day).strftime("%A")
                        actual, _ = calculate_weekday(year, month, day)
                        self.assertEqual(expected, actual)
