# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:16:45 2022

@author: Luke

Help the frog to find a way to freedom You have an array of integers and have a frog at the first position [Frog, int, int, int, ..., int] The integer itself may tell you the length and the direction of the jump For instance: 2 = jump two indices to the right -3 = jump three indices to the left 0 = stay at the same position Your objective is to find how many jumps are needed to jump out of the array. Return -1 if Frog can't jump out of the array Example: array = [1, 2, 1, 5]; jumps = 3 (1 -> 2 -> 5 -> ) All tests for this Kata are randomly generated.
"""

def solution(a):
    # your code here
    if a[0] == 0:
        return -1
    else:
        count = 0
        i = 0
        while i < len(a) and count<len(a)*100:
            count += 1
            i += a[i]
            if i >= len(a) or i<0:
                return count
            if a[i] == 0:
                return -1
    return -1

print(solution([1, 2, 1, 5])) # Test from the prompt. Answer should be 3. 
print(solution([1, 2, 1, -1])) # The answer should be -1 because the frog will jump from 1 -> 2 -> -1 -> 1 -> -1 -> 1 in a neverending loop between 1 and -1
print(solution([1, 2, 5, -1, 4, 6, 3, -4])) # The answer should be -1 because the the frog will get stuck in a loop from 5 -> -4 -> -1 -> 5
print(solution([-1, 2, 5, 2, 4, 6, 3, 4])) # The answer should be 1 because the frog will jump out from the left on the first move.
print(solution([1, 2, 5, 2, 4, -3, 3, 1, -2, 1])) # The answer should be 9 because the frog will jump out in this order: 1 -> 2 -> 2 -> -3 -> 5 -> 1 -> -2 -> 3 -> 1 -> out