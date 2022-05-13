# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:26:32 2022

@author: Luke

Create a function to multiply all of the values in a list by the amount of values in the given list.
Examples
MultiplyByLength([2, 3, 1, 0]) ➞ [8, 12, 4, 0]
MultiplyByLength([4, 1, 1]) ➞ ([12, 3, 3])
MultiplyByLength([1, 0, 3, 3, 7, 2, 1]) ➞  [7, 0, 21, 21, 49, 14, 7]
MultiplyByLength([0]) ➞ ([0])
Notes
All of the values given are numbers.
All lists will have at least one element.
Don't forget to return the result.
"""

def MultiplyByLength(arr):
    return [i*len(arr) for i in arr]

print(MultiplyByLength([2,3,1,0]))
print(MultiplyByLength([4,1,1]))
print(MultiplyByLength([1,0,3,3,7,2,1]))
print(MultiplyByLength([0]))
print(MultiplyByLength([1337,420,69,13]))
