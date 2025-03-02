import unittest

from coe_number.fizzbuzz_utils import FizzBuzz


class fizzbuzztest(unittest.TestCase):
    def test_give_15_30_is_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")

    def test_give_6_12_is_fizz(self):
        self.assertEqual(FizzBuzz(6), "Fizz")
        self.assertEqual(FizzBuzz(12), "Fizz")

    def test_give_5_20_is_buzz(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(20), "Buzz")

    def test_give_4_8_is_not_match(self):
        self.assertEqual(FizzBuzz(4), "Not match")
        self.assertEqual(FizzBuzz(8), "Not match")

    def test_give_3_5_15_is_not_not_match(self):
        self.assertNotEqual(FizzBuzz(3), "Not match")
        self.assertNotEqual(FizzBuzz(5), "Not match")
        self.assertNotEqual(FizzBuzz(15), "not match")
