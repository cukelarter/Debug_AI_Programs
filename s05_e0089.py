# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:09:49 2022

@author: Luke

Task Determine the client's membership level based on the invested amount of money and the given thresholds for membership levels. There are four membership levels (from highest to lowest): Platinum, Gold, Silver, Bronze The minimum investment is the threshold limit for Bronze membership. If the given amount is less than the Bronze treshold limit return Not a member. A client belongs to a membership level when his invested amount is greater than or equal the level's threshold amount. Examples: |--------+----------+------+--------+--------+--------------+------------------| | Amount | Platinum | Gold | Silver | Bronze | Result | Explanations | |--------+----------+------+--------+--------+--------------+------------------| | 7000 | 10000 | 8000 | 6000 | 4000 | Silver | Amount >= Silver | | 3000 | 10000 | 8000 | 6000 | 5000 | Not a member | Amount < Bronze | | 8000 | 12000 | 8000 | 7000 | 5000 | Gold | Amount >= Gold | |--------+----------+------+--------+--------+--------------+------------------| Restrictions The first line of your code has to be def membership(amount, platinum, gold, silver, bronze): Your code except for the firt line mustn't contain the words platinum, gold, silver, bronze or they reversed forms (e.g. dlog) or any string which contains these words or they reversed forms. (The check is case-insensitive.) Must not contain: +, %, {, }. Disclaimer This kata is about creativity not proper coding style. Your colleagues/boss won't like you if you make production code like this. :) Don't forget to rate the kata after you finish it. :) Happy coding! suic
"""

def membership(amount, platinum, gold, silver, bronze):
    if amount < bronze:
        return "Not a member"
    elif amount >= platinum:
        return "Platinum"
    elif amount >= gold:
        return "Gold"
    elif amount >= silver:
        return "Silver"
    else:
        return "Bronze"
    
print(membership(7000,10000,8000,6000,4000)) #expect 'Silver'
print(membership(3000,10000,8000,6000,4000)) #expect 'not a member'
print(membership(8000,10000,8000,6000,4000)) #expect 'Gold'
print(membership(12000,10000,8000,6000,4000)) #expect 'Platinum
print(membership(7000,50000,40000,30000,5000)) #expect 'Bronze'