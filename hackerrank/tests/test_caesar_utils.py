import unittest
from prob.caesar_utils import caesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_large_k(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")
        self.assertEqual(caesarCipher("xyz", 28), "zab")

    def test_special_characters(self):
        self.assertEqual(caesarCipher("123-@!", 3), "123-@!")
