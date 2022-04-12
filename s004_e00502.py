# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 00:11:26 2022

@author: cukel

 John learns to play poker with his uncle. His uncle told him: Poker to be in accordance with the order of "2 3 4 5 6 7 8 9 10 J Q K A". The same suit should be put together. But his uncle did not tell him the order of the four suits. 
 
 Give you John's cards and Uncle's cards(two string `john` and `uncle`). Please reference to the order of Uncle's cards, sorting John's cards. 
 
 
# Examples

```
For Python:

Suits are defined as S, D, H, C.

sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S2S3S5HJHQHKC8C9C10D4D5D6D7")
should return "S3SJSKSAH2H5H10C5C7CQD2D5D6"
sort_poke("D6H2S3D5SJCQSKC7D2C5H5H10SA","C8C9C10D4D5D6D7S2S3S5HJHQHK") 
should return "C5C7CQD2D5D6S3SJSKSAH2H5H10" 

wtf does this mean?
"""

johnhand='D6H2S3D5SJCQSKC7D2C5H5H10SA'
unclehand='C8C9C10D4D5D6D7S2S3S5HJHQHK'
import re

def sort_poker(john, uncle):
    # first find the order of the uncle's cards
    suits=['C','S','H','D']
    suitorder=[x for x in uncle if any([x==suit for suit in suits])]
    # map to dictionary for sorting later
    suitorder={suitorder[ii]:ii for ii in range(len(suitorder))}
    # get default order of cards
    possible_cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardorder={possible_cards[ii]:ii for ii in range(len(possible_cards))}
    # get john's cards as list
    jsplit=[e for e in re.split('([D|C|H|S])',john) if e]
    j=[''.join(jsplit[ii:ii+2]) for ii in range(0,len(jsplit),2)]
    # now sort his cards by uncle's order
    #return ''.join(sorted(j, key=lambda x: suitorder[x[0]]))
    return ''.join(sorted(j, key=lambda x: (suitorder[x[0]],cardorder[x[1:]])))

if __name__=='__main__':
    print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S2S3S5HJHQHKC8C9C10D4D5D6D7"))
    print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","C8C9C10D4D5D6D7S2S3S5HJHQHK"))
    print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","H2H3H5SJSQSKC8C9C10D4D5D6D7"))
    print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S8S9S10D4D5D6D7C2C3C5HJHQHK"))
    print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","H2H3H5SJSQSKD8D9D10C4C5C6C7"))