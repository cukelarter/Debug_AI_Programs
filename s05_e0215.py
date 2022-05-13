# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:52:10 2022

@author: Luke
"""

def magicalString(n):
    if n == 0:
        return 0
    if n <= 3:
        return 1
    s = [1, 2, 2]
    i = 2
    while len(s) < n:
        s += [3 - s[-1]] * s[i]
        i += 1
    return s[:n].count(1)

print(magicalString(6))     # expect 3 ([1, 2, 2, 1, 1, 2])
print(magicalString(8))     # expect 4 ([1, 2, 2, 1, 1, 2, 1, 2])
print(magicalString(10))    # expect 5 ([1, 2, 2, 1, 1, 2, 1, 2, 2, 1])
print(magicalString(14))    # expect 7 ([1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1])
print(magicalString(20))    # expect 10([1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1])