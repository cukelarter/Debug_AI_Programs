# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:21:18 2022

@author: Luke

Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory and all of mathematics. It states: Every even integer greater than 2 can be expressed as the sum of two primes. For example: 6 = 3 + 3 8 = 3 + 5 10 = 3 + 7 = 5 + 5 12 = 5 + 7 Some rules for the conjecture: pairs should be descending like [3,5] not [5,3] all pairs should be in ascending order based on the first element of the pair: [[5, 13], [7, 11]] is accepted but [[7, 11],[5, 13]] is not accepted. Write the a function that find all identical pairs of prime numbers: def goldbach(even_number) You should return an array of containing pairs of primes, like: [[5, 13], [7, 11]] # even_number = 18 or [[3, 31], [5, 29], [11, 23], [17, 17]] # even_number = 34
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

print(sieve(7))     # expect [2,3,5]
print(sieve(8))     # expect [2,3,5,7]
print(sieve(3))     # expect [2]
print(sieve(1))     # expect []

def goldbach(even_number):
    primelist=sieve(even_number)
    ii=0; testprime=primelist[ii]
    pairs=[]
    while testprime<=even_number/2:
        checkprime = even_number-testprime
        if checkprime in primelist: # if valid prime
            pairs.append([testprime, checkprime])
        ii+=1; testprime=primelist[ii]
    return pairs

print(goldbach(6))              # expect [[3,3]]
print(goldbach(10))             # expect [[3,7],[5,5]]
print(goldbach(12))             # expect [[5,7]]
print(goldbach(18))             # expect [[5,13],[7,11]]
print(goldbach(34))             # expect [[3,31],[5,29],[11,23],[17,17]]