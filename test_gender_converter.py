from unittest import TestCase

from gender_converter import convert_gender


class Test(TestCase):
    def test_convert_gender_when_male(self):
        actual = convert_gender("M")
        expected = "MALE"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
        actual = convert_gender("F")
        expected = "FEMALE"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_unknown(self):
        actual = convert_gender("hello")
        expected = "UNKNOWN_GENDER"
        self.assertEqual(actual, expected)
