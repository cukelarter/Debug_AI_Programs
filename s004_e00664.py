# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:07:49 2022

@author: cukel

This kata is inspired by Project Euler Problem #387

A Harshad number (or Niven number) is a number that is divisible by the sum of its digits. A right truncatable Harshad number is any Harshad number that, when recursively right-truncated, results in a Harshad number at each truncation. By definition, 1-digit numbers are not right truncatable Harshad numbers.

For example 201 (which is a Harshad number) yields 20, then 2 when right-truncated, which are all Harshad numbers. Thus 201 is a right truncatable Harshad number.
Your task

Given a range of numbers ((a, b), both included), return the list of right truncatable Harshad numbers in this range.

Note: there are `500` random tests, with 0 <= `a` <= `b` <= 10^(16)

Note: there are `500` random tests, with `0 <= a <= b <= Number.MAX_SAFE_INTEGER`

Examples

0, 20        -->  [10, 12, 18, 20]
30, 100      -->  [30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100]
90, 200      -->  [90, 100, 102, 108, 120, 126, 180, 200]
200, 210     -->  [200, 201, 204, 207, 209, 210]
1000, 2000   -->  [1000, 1002, 1008, 1020, 1026, 1080, 1088, 1200, 1204, 1206, 1260, 1800, 2000]
2200, 2300   -->  []
9000002182976, 9000195371842  -->  [9000004000000, 9000004000008]
"""



def rthn_between(a, b):
    return [i for i in range(a, b+1) if is_rthn(i)]

def is_rthn(n):
    if n < 10:
        return False
    while n > 0:
        if n % sum(map(int, str(n))) != 0:
            return False
        n //= 10
    return True