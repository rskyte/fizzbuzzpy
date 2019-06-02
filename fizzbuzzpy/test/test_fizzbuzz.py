#!/usr/bin/env python3
import sys
import unittest
sys.path.append('./fizzbuzzpy')
from src.fizzbuzz import fizzbuzz

class FizzbuzzTest(unittest.TestCase):
    def test_returns_fizz_for_multiple_of_3(self):
        value = fizzbuzz(3)
        self.assertEqual(value, 'fizz', 'incorrect value')

if __name__ == '__main__':
    unittest.main()