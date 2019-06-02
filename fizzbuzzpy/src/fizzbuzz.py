#!/usr/bin/env python3

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'