#!/usr/bin/env python3

def fizzbuzz(num):
    if num == 0:
        return '0'
    elif num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'
    else:
        return str(num)
    