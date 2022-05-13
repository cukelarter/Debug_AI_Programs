# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:45:50 2022

@author: cukel

The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).

In C++ return in such a case {0, 0}. In F# return [||]. In Kotlin return []

#Examples: gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin return[]`

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.

"""


# use the sieve of eratosthenes to return list of primes
def sieve(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes=[p for p in range(2,n+1) if prime[p]]
    return primes

def gap(g,m,n):
    # call sieve to get all primes below upper bound n
    # then remove all primes less than lower bound m
    primes=[x for x in sieve(n) if x>=m]
    print(primes)
    # we could use numpy to subtract but this way 
    # requires no imports to get gaps between primes
    gaps=[primes[ii+1]-primes[ii] for ii in range(0,len(primes)-1)]
    if g in gaps:
        idx = gaps.index(g)
        return (primes[idx],primes[idx+1])
    else:
        return (0,0)