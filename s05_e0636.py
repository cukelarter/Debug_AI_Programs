# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:07:12 2022

@author: Luke

Task You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make? Example For a = 1, b = 2 and n = 2, the output should be 8 You will cast your first marble and get  2,๐๐๐ก๐๐๐คโ๐๐โ๐กโ๐๐๐ข๐๐๐๐๐ ๐ค๐๐๐๐๐๐๐๐๐2๐๐๐3.๐โ๐๐๐ฆ๐๐ข๐๐๐ ๐ก๐ฆ๐๐ข๐๐ ๐๐๐๐๐๐๐๐๐๐๐,๐กโ๐๐ค๐๐๐๐ค๐๐๐๐๐๐ฃ๐๐ฆ๐๐ข 6. Overall, you'll make $8. So, the output is 8. Input/Output [input] integer a Constraints: 1 โค a โค 2000 [input] integer b Constraints: 1 โค b โค 2000 [input] integer n The number of magic marbles in your possession, a non-negative integer. Constraints: 0 โค n โค 5 [output] an integer
"""

def magical_well(a, b, n):
    return sum((a+i)*(b+i) for i in range(n))

print(magical_well(1,2,2))          # expect 8  ((1*2)+(2*3))
print(magical_well(1,2,3))          # expect 20 (8+(3*4))
print(magical_well(10,10,0))        # expect 0 
print(magical_well(2000,2000,1))    # expect 4e6 (2000*2000)
print(magical_well(2000,2000,2))    # expect 8004001 (4e6+(2000*2000))
print(magical_well(1,1,5))          # expect 55 ((1*1)+(2*2)+...(5*5))



