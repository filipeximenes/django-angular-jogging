# coding: utf-8

from django.test import TestCase

from timings.timing_conversion import (
    from_seconds_to_formated, from_formated_to_seconds)


class FromSecondsToFormated(TestCase):

    def test_converts_seconds(self):
        result = from_seconds_to_formated(30)

        self.assertEqual(result, '0:0:30')

    def test_converts_minutes(self):
        result = from_seconds_to_formated(134)

        self.assertEqual(result, '0:2:14')

    def test_converts_hours(self):
        result = from_seconds_to_formated(3734)

        self.assertEqual(result, '1:2:14')

    def test_converts_many_hours(self):
        result = from_seconds_to_formated(90134)

        self.assertEqual(result, '25:2:14')


class FromFormatedToSeconds(TestCase):

    def test_converts_seconds(self):
        result = from_formated_to_seconds('0:23')

        self.assertEqual(result, 23)

    def test_converts_minutes(self):
        result = from_formated_to_seconds('2:23')

        self.assertEqual(result, 143)

    def test_converts_hours(self):
        result = from_formated_to_seconds('1:0:23')

        self.assertEqual(result, 3623)

    def test_requires_at_least_minutes(self):
        result = from_formated_to_seconds('23')

        self.assertEqual(result, False)
