# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:04:20 2022

@author: Luke

Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2: 1+1+1+1, 1+1+2, 2+2. The order of coins does not matter: 1+1+2 == 2+1+1 Also, assume that you have an infinite amount of coins. Your function should take an amount to change and an array of unique denominations for the coins: count_change(4, [1,2]) # => 3 count_change(10, [5,2,3]) # => 4 count_change(11, [5,7]) # => 0
"""

def count_change(money, coins):
    # if money is 0, return 1
    if money == 0:
        return 1
    # if money is less than 0, return 0
    if money < 0:
        return 0
    # if coins is empty, return 0
    if not coins:
        return 0
    # return the sum of the count_change function with the first coin removed and the money
    # minus the first coin, and the count_change function with the first coin removed and
    # the money
    return count_change(money - coins[0], coins) + count_change(money, coins[1:])


print(count_change(4,[1,2]))    # expect 3
print(count_change(10,[5,2,3])) # expect 4
print(count_change(11,[5,7]))   # expect 0

print(count_change(5,[1,2,3,5]))# expect 6
# 1+1+1+1+1, 2+1+1+1, 3+1+1, 2+2+1, 3+2, 5
print(count_change(18,[2,3,9])) # expect 7
# 2*9, 3*6, 9*2, 9+3*3, 2*6+3*2, 3*4+2*3,9+3+2*3