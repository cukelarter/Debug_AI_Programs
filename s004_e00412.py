# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:15:38 2022

@author: Luke

Task
Create a function that given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases.

In the event that an element appears more than once in the input sequence, only one of them will be taken into account for the result, discarding the rest.

Input
Sequence of strings. Valid characters for those strings are uppercase and lowercase characters from the alphabet and whitespaces.

Output
Sequence of elements. Each element is the group of inputs that can be obtained by rotating the strings.

Sort the elements of each group alphabetically.

Sort the groups descendingly by size and in the case of a tie, by the first element of the group alphabetically.

Examples
['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] --> [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
"""

def group_cities(seq):
    """
    Given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases.
    """
    # Create a dictionary with the lowercase string as key and the original string as value.
    d = {s.lower(): s for s in seq}
    # Create a set with the lowercase strings.
    s = set(d.keys())
    # Create a list with the values of the dictionary.
    l = list(d.values())
    # Create a list with the groups of strings.
    groups = []
    # Iterate over the lowercase strings.
    for s1 in s:
        # Create a list with the strings that can be obtained by rotating the string.
        group = [d[s1]]
        # Iterate over the lowercase strings.
        for s2 in s:
            # Check if the string can be obtained by rotating the string.
            if s1 != s2 and s1 in s2 * 2:
                # Add the string to the list, but use the proper name
                group.append(d[s2])
        # sort internal group alphabetically
        group.sort()
        # only append if it doesn't match a set already stored
        if not any([set(g)==set(group) for g in groups]):
            groups.append(group)
    # sort list of groups by size
    groups.sort(key=len)
    # key = len returns the oppopsite of what we're looking for, so reverse
    groups=list(reversed(groups))
    return groups
    
    
t1 = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
t2 = ['Rome', 'Rome', 'Rome', 'Donlon', 'London']