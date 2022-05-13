# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:02:18 2022

@author: Luke

Create a function that takes a string as its argument and returns the string in reversed order.
Examples
reverse("Hello World") ➞ "dlroW olleH"
reverse("The quick brown fox.") ➞ ".xof nworb kciuq ehT"
reverse("Edabit is really helpful!") ➞ "!lufpleh yllaer si tibadE"
Notes
You can expect a valid string for all test cases.

"""

def reverse(txt):
    return txt[::-1]

print(reverse("Hello World"))                   # expect "dlroW olleH"
print(reverse("The quick brown fox."))          # expect ".xof nworb kciuq ehT"
print(reverse("Edabit is really helpful!"))     # expect "!lufpleh yllaer si tibadE"
print(reverse('tacocat1'))                      # expect "1tacocat"
print(reverse('redrum'))                        # expect "murder"-The passport does not have a recognised front cover (unless it's just very worn like mine...).
