# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:57:52 2022

@author: Luke

Prompt
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog" Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish" Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog" Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog" Output: false

Notes: You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
        return True