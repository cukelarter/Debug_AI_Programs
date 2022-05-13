# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:38:54 2022

@author: Luke

You have a two-dimensional list in the following format: data = [[2, 5], [3, 4], [8, 7]] Each sub-list contains two items, and each item in the sub-lists is an integer. Write a function process_data() that processes each sub-list like so: [2, 5] --> 2 - 5 --> -3 [3, 4] --> 3 - 4 --> -1 [8, 7] --> 8 - 7 --> 1 and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3. For input, you can trust that neither the main list nor the sublists will be empty.
"""

def process_data(data):
    result = 1
    for sublist in data:
        result *= sublist[0] - sublist[1]
    return result

print(process_data([[1,1],[2,3],[4,5]]))            # expect 0
print(process_data([[1,4],[7,3],[4,2]]))            # expect 24
print(process_data([[801,1],[-900,-100],[2,5]]))    # expect 1920000 (800*800*3)
print(process_data([[1,2],[2,3],[4,5],[6,7],[8,9]])) # expect -1
print(process_data([[1,1]]))                        # expect 0