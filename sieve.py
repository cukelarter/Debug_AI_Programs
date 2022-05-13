# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:46:13 2022

@author: Luke
"""

# use the sieve of eratosthenes to return list of primes
def sieve(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    prime = [True for i in range(n)]
    p = 2
    while(p * p <= n):
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n, p):
                prime[i] = False
        p += 1
    primes=[p for p in range(2,n) if prime[p]]
    return primes