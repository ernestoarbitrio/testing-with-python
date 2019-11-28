from src.datetime_utils import is_weekday, is_summer
from unittest.mock import Mock
from unittest.mock import patch, Mock
from unittest import TestCase
from datetime import datetime


def test_is_weekday_to_help():
    assert is_weekday()


class IsSummerTests(TestCase):
    AUGUST = 8
    DECEMBER = 12

    @patch("src.datetime_utils.get_now")
    def test_is_summer_in_august(self, now_mock):
        now_mock.return_value = datetime(year=2000, month=self.AUGUST, day=1)

        self.assertTrue(is_summer())

    @patch("src.datetime_utils.get_now")
    def test_is_summer_in_december(self, now_mock):
        now_mock.return_value = datetime(year=2000, month=self.DECEMBER, day=1)

        self.assertFalse(is_summer())


class IsWeekDayTests(TestCase):
    @patch("src.datetime_utils.get_today")
    def test_is_weekday(self, weekday_mock):
        weekday_mock.return_value = datetime(year=2019, month=1, day=1)

        self.assertTrue(is_weekday())

    @patch("src.datetime_utils.get_today")
    def test_is_not_weekday(self, weekday_mock):
        not_weekday_datetime = datetime(year=2019, month=1, day=6)

        weekday_mock.return_value = not_weekday_datetime

        self.assertFalse(is_weekday())
