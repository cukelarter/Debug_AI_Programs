# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j),
we take the bitwise OR of all the elements in B, obtaining a result A[i] |
A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once
are only counted once in the final answer.)

Example 1:

    Input: [0]
    Output: 1
    Explanation:
    There is only one possible result: 0.

Example 2:

    Input: [1,1,2]
    Output: 3
    Explanation:
    The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
    These yield the results 1, 1, 2, 1, 3, 3.
    There are 3 unique values, so the answer is 3.

Example 3:

    Input: [1,2,4]
    Output: 6
    Explanation:
    The possible results are 1, 2, 3, 4, 6, and 7.

Note:

    1. 1 <= A.length <= 50000
    2. 0 <= A[i] <= 10^9
"""

def subarrayBitwiseORs(A):
    if not A:
        return 0

    res = set()
    cur = set()
    for a in A:
        cur = {a | b for b in cur} | {a}
        res |= cur
    return len(res)

print(subarrayBitwiseORs([0])) # expect 1
print(subarrayBitwiseORs([1,1,2])) # expect 3
print(subarrayBitwiseORs([1,2,4])) # expect 6
print(subarrayBitwiseORs([1,2,4,4,4,4,4])) # expect 6
print(subarrayBitwiseORs([3,3,2,5,7,])) # expect 4

subarrayBitwiseORs([4]*50000) # expect 1 since only one type of entry in list
subarrayBitwiseORs([4,2,4,2]) # expect 3 since it will only ever be
                              # 4 (100) | 2 (010) = 6 (110)
                              # or identical operations (i|i = i)
subarrayBitwiseORs([10**9,10**7,10**5]) # expect 6, testing max values