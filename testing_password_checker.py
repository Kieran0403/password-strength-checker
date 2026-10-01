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

class TestPasswordCheckerCharacterTypes(unittest.TestCase):
    """Unit tests for uppercase, lowercase, numbers, and special characters.
    
    Using assertFalse to check they also fail correctly"""

    def test_uppercase(self):
        self.assertTrue(PasswordChecker("helloWorld").check_uppercase())
        self.assertFalse(PasswordChecker("helloworld").check_uppercase())

    def test_lowercase(self):
        self.assertTrue(PasswordChecker("HELLOWORLd").check_lowercase())
        self.assertFalse(PasswordChecker("HELLOWORLD").check_lowercase())

    def test_numbers(self):
        self.assertTrue(PasswordChecker("pass123").check_numbers())
        self.assertFalse(PasswordChecker("password").check_numbers())

    def test_special_characters(self):
        self.assertTrue(PasswordChecker("hello@world!").check_special_characters())
        self.assertFalse(PasswordChecker("helloworld123").check_special_characters())
