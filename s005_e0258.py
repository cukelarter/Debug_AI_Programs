# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:05:20 2022

@author: Luke

Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. Watch out for strings!
Examples
count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
# 1+1+1+1
count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4
count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6
Notes
The data might be dirty! Clean out any filthy strings.
"""

def count_missing_nums(lst):
    lst = [int(x) for x in lst if x.isdigit()]
    return len(range(min(lst), max(lst)+1)) - len(lst)

print(count_missing_nums(["1", "3", "5", "7", "9"])) # expect 4
print(count_missing_nums(["7", "3", "1", "9", "5"])) # expect 4
print(count_missing_nums(["1", "5", "B", "9", "z"])) # expect 6
print(count_missing_nums(["1", "5", "B", "9", "z","6","7","8"])) # expect 3
print(count_missing_nums(["3", "20"]))               # expect 16