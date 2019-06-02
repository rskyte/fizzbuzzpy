#!/usr/bin/env python3
import sys
import unittest
sys.path.append('./fizzbuzzpy')
from src.fizzbuzz import fizzbuzz

class FizzbuzzTest(unittest.TestCase):
    def test_returns_fizz_for_multiple_of_3(self):
        value = fizzbuzz(3)
        value2 = fizzbuzz(9)
        self.assertEqual(value, 'fizz', 'incorrect value')
        self.assertEqual(value2, 'fizz', 'incorrect value')

    def test_returns_fizz_for_multiple_of_5(self):
        value = fizzbuzz(5)
        value2 = fizzbuzz(25)
        self.assertEqual(value, 'buzz', 'incorrect value')
        self.assertEqual(value2, 'buzz', 'incorrect value')

if __name__ == '__main__':
    unittest.main()