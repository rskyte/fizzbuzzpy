#!/usr/bin/env python3
import sys
import unittest
sys.path.append('./fizzbuzzpy')
from src.fizzbuzz import fizzbuzz

FAILURE = 'incorrect value'

class FizzbuzzTest(unittest.TestCase):
    def test_returns_fizz_for_multiple_of_3(self):
        value = fizzbuzz(3)
        value2 = fizzbuzz(9)
        self.assertEqual(value, 'fizz', FAILURE)
        self.assertEqual(value2, 'fizz', FAILURE)

    def test_returns_fizz_for_multiple_of_5(self):
        value = fizzbuzz(5)
        value2 = fizzbuzz(25)
        self.assertEqual(value, 'buzz', FAILURE)
        self.assertEqual(value2, 'buzz', FAILURE)

    def test_returns_fizzbuzz_for_multiple_of_3_and_5(self):
        value = fizzbuzz(15)
        value2 = fizzbuzz(75)
        self.assertEqual(value, 'fizzbuzz', FAILURE)
        self.assertEqual(value2, 'fizzbuzz', FAILURE)

    def test_returns_zero_for_zero(self):
        value = fizzbuzz(0)
        self.assertEqual(value, '0', FAILURE)

    def test_returns_original_number(self):
        value = fizzbuzz(1)
        value2 = fizzbuzz(74)
        self.assertEqual(value, '1', FAILURE)
        self.assertEqual(value2, '74', FAILURE)

if __name__ == '__main__':
    unittest.main()