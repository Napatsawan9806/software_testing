import unittest
from prob.alternate_utils import alternate


class TestAlternate(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("abcabc"), 4)

    def test_no_valid_pairs(self):
        self.assertEqual(alternate("x"), 0)
        self.assertEqual(alternate("xyz"), 2)

    def test_max_length(self):
        self.assertEqual(alternate("abababab"), 8)
        self.assertEqual(alternate("aabbccddeeffgghh"), 0)


# 100% test coverage
