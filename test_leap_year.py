import unittest
import leap_year


class TestLeapYear(unittest.TestCase):

    # Tests for leap years
    def test_1(self):
        self.assertEqual(leap_year.is_leapyear(2000), True)
        self.assertEqual(leap_year.is_leapyear(2016), True)

    # Tests for non leap years
    def test_2(self):
        self.assertEqual(leap_year.is_leapyear(2013), False)
        self.assertEqual(leap_year.is_leapyear(2100), False)

    # Test invalid inputs
    def test_3(self):
        self.assertRaises(TypeError, leap_year.is_leapyear("2000"))
