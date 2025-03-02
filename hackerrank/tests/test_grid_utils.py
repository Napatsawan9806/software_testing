import unittest
from prob.grid_utils import gridChallenge


class TestGridChallenge(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["abcde"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["a", "b", "c", "d"]), "YES")
