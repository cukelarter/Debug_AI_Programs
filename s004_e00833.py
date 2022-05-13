# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:00:58 2022

@author: Luke

You are given an array  𝑎  consisting of  𝑛  integers (it is guaranteed that  𝑛  is even, i.e. divisible by  2 ). All  𝑎𝑖  does not exceed some integer  𝑘 .

Your task is to replace the minimum number of elements (replacement is the following operation: choose some index  𝑖  from  1  to  𝑛  and replace  𝑎𝑖  with some integer in range  [1;𝑘] ) to satisfy the following conditions: after all replacements, all  𝑎𝑖  are positive integers not greater than  𝑘 ; for all  𝑖  from  1  to𝑓𝑟𝑎𝑐𝑛2the following equation is true:  𝑎𝑖+𝑎𝑛−𝑖+1=𝑥 , where  𝑥  should be the same for all𝑓𝑟𝑎𝑐𝑛2pairs of elements.

You have to answer  𝑡  independent test cases.

-----Input-----

The first line of the input contains one integer  𝑡  (1𝑙𝑒𝑡𝑙𝑒104) — the number of test cases. Then  𝑡  test cases follow.

The first line of the test case contains two integers  𝑛  and  𝑘  (2𝑙𝑒𝑛𝑙𝑒2𝑐𝑑𝑜𝑡105,1𝑙𝑒𝑘𝑙𝑒2𝑐𝑑𝑜𝑡105) — the length of  𝑎  and the maximum possible value of some  𝑎𝑖  correspondingly. It is guratanteed that  𝑛  is even (i.e. divisible by  2 ). The second line of the test case contains  𝑛  integers𝑎1,𝑎2,𝑑𝑜𝑡𝑠,𝑎𝑛(1𝑙𝑒𝑎𝑖𝑙𝑒𝑘), where  𝑎𝑖  is the  𝑖 -th element of  𝑎 .

It is guaranteed that the sum of  𝑛  (as well as the sum of  𝑘 ) over all test cases does not exceed2𝑐𝑑𝑜𝑡105(𝑠𝑢𝑚𝑛𝑙𝑒2𝑐𝑑𝑜𝑡105,𝑠𝑢𝑚𝑘𝑙𝑒2𝑐𝑑𝑜𝑡105).

-----Output-----

For each test case, print the answer — the minimum number of elements you have to replace in  𝑎  to satisfy the conditions from the problem statement.

-----Example----- Input 4 4 2 1 2 1 2 4 3 1 2 2 1 8 7 6 1 1 7 6 3 4 6 6 6 5 2 6 1 3 4

Output 0 1 4 2
"""

def main():
    # Read the number of test cases.
    t = int(input())
    # Solve all test cases.
    for _ in range(t):
        # Read the input.
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        # Compute and print the answer.
        print(solve(n, k, a))

def solve(n, k, a):
    # Compute the number of elements to replace.
    pairs=get_pairs(a)
    test_x=[sum(pair) for pair in pairs] # get starting x values
    if test_x.count(test_x[0]) == len(test_x): # if test xs are equal no change necessary
        return 0
    else:
        for ii in range(len(test_x)):
            x=test_x[ii]
            test_pairs = pairs[:ii]+pairs[ii+1:]
            offset = sum([sum(pair)==x for pair in test_pairs]) # accounts for x of test pair matching x of other pairs
            
            if all([canReformat(pair,x,k) for pair in test_pairs]):
                # if all can be reformatted to x, return how many pairs need modification
                return int(n/2-1-offset)
        return int(n/2) # solution requires changing every pair


def canReformat(pair, x, k):
    # Determine if any number of a pair of numbers can be replaced
    # such that the new pair is equal to x, and the replacing number is less than k
    a1,a2=pair
    # calculate all possible pairs that can be generated through replacement
    pairsums1=[a1+c for c in range(1,k+1)]
    pairsums2=[a2+c for c in range(1,k+1)]
    psums=pairsums1+pairsums2
    return x in psums

def get_pairs(a):
    # Retreives pairs from array a
    return [(a[i],a[len(a)-i-1]) for i in range(0,int(len(a)/2))]
        
if __name__=='__main__':
    main()
    
#%%
    
    
b=[(a[i],a[len(a)-i-1]) for i in range(0,int(len(a)/2))]
