# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:02:07 2022

Prompt

Write a program that will take a string of digits and give you all the possible consecutive slices of length n in that string.

Raise an error if n is larger than the length of the string.
Examples

For example, the string "01234" has the following 2-digit slices:

[0, 1], [1, 2], [2, 3], [3, 4]

The same string has the following 4-digit slices:

[0, 1, 2, 3], [1, 2, 3, 4]

@author: cukel
"""



def series_slices(digits, n):
    """Return a list of consecutive slices of length `n` from `digits`."""
    if n > len(digits):
        raise ValueError("n cannot be greater than the length of the digits string")
    unformatted=[digits[i:i+n] for i in range(len(digits)-n+1)]
    return [[int(char) for char in entry] for entry in unformatted]
    #return [[int(char) for char in entry] for entry in [digits[i:i+n] for i in range(len(digits)-n+1)]]
print(series_slices('01234',2))
print(series_slices('01234',4))
print(series_slices('123456789',6))
print(series_slices('121',1))
print(series_slices('',1))