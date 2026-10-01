import unittest
from password_checker import PasswordChecker

class TestPasswordCheckerLength(unittest.TestCase):
    """Unit tests for the length evaluation method.
    
    The assertEqual is a unittest method to check is the answer produced is the same as the expected one"""

    def test_short_password(self):
        checker = PasswordChecker("Short1!")
        self.assertEqual(checker.check_length(), 0)

    def test_minimum_acceptable_length(self):
        checker = PasswordChecker("12345678")
        self.assertEqual(checker.check_length(), 1)

    def test_bonus_length(self):
        checker = PasswordChecker("A1b!C2d#E3f$G4h%")
        self.assertEqual(checker.check_length(), 2) #The 2 represents the points returned, NOT the lenth of string