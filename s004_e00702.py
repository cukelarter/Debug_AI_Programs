# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:10:26 2022

@author: cukel

Prompt

The round carousel consists of 𝑛
figures of animals. Figures are numbered from 1 to 𝑛 in order of the carousel moving. Thus, after the 𝑛-th figure the figure with the number 1 follows. Each figure has its own type — the type of the animal corresponding to this figure (the horse, the tiger and so on). The type of animal of the 𝑖-th figure equals 𝑡𝑖. [Image] The example of the carousel for 𝑛=9 and 𝑡=[5,5,1,15,1,5,5,1,1]

.

You want to color each figure in one of the colors. You think that it's boring if the carousel contains two different figures (with the distinct types of animals) going one right after another and colored in the same color.

Your task is to color the figures in such a way that the number of distinct colors used is the minimum possible and there are no figures of the different types going one right after another and colored in the same color. If you use exactly 𝑘
distinct colors, then the colors of figures should be denoted with integers from 1 to 𝑘.
"""


def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        t = list(map(int, input().split()))
        c = [0] * n
        for i in range(n):
            if i == 0:
                c[i] = 1
            else:
                if t[i] == t[i - 1]:
                    c[i] = c[i - 1]
                else:
                    c[i] = c[i - 1] + 1
        print(c[-1])
        print(*c)

#%% 
        
def main(t):
    k=len(set(t)) # get number of unique entries
    n=len(t)
    if k>1:
        if n%2==0:
            outlist=[1,2]*int(n/2)
        else:
            outlist=[1]+[2,1]*int((n-1)/2)
        return (2, outlist)
    else: # only one figure type
        return (1, [1]*n)