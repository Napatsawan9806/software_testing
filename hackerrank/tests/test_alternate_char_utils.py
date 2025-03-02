import unittest
from prob.alternate_char_utils import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternatingCharacters("AABAAB"), 2)
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)


# 100% test coverage
