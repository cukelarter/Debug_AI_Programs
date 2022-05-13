# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:36:57 2022

@author: Luke

It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case. To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.
"""

def modulus(n):
    if isinstance(n,int):
        return n % 2
    else:
        return -1
    

print(modulus(4))           # expect 0
print(modulus(5.0))         # expect -1
print(modulus(-101))        # expect 1
print(modulus(1.32511))     # expect -1
