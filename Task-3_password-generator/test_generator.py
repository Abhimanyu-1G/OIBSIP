import unittest
from generator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_length(self):
        password = self.generator.generate(length=16)
        self.assertEqual(len(password), 16)

    def test_uppercase(self):
        password = self.generator.generate(use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertFalse(any(c in string.ascii_lowercase for c in password))

    def test_digits(self):
        password = self.generator.generate(use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
        self.assertTrue(any(c in string.digits for c in password))

    def test_all_options(self):
        password = self.generator.generate(length=20, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))

    def test_strength_check(self):
        weak_pass = "abc"
        strong_pass = "Abc1!@#$"
        
        strength, color = self.generator.check_strength(weak_pass)
        self.assertEqual(strength, "Weak")
        
        strength, color = self.generator.check_strength(strong_pass)
        self.assertNotEqual(strength, "Weak")

if __name__ == '__main__':
    unittest.main()
