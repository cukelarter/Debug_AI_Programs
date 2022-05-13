# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:43:52 2022

@author: Luke
Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime. Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself. Example is_prime(1) /* false / is_prime(2) / true / is_prime(-1) / false */ Assumptions You can assume you will be given an integer input. You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0). There are no fancy optimizations required, but still the most trivial solutions might time out. Try to find a solution which does not loop all the way up to n.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(is_prime(1))          # expect False
print(is_prime(2))          # expect True
print(is_prime(-1))         # expect False
print(is_prime(11))         # expect True
print(is_prime(10**308))    # expect False