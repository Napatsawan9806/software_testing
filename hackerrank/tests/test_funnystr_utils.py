import unittest
from prob.funnystr_utils import funnyString


class TestFunnyString(unittest.TestCase):
    def test_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("lmno"), "Funny")

    def test_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("ivvkx"), "Not Funny")
