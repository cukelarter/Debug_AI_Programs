# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:51:18 2022

@author: Luke

Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year. Find the number of Friday 13th in the given year. Input: Year as an integer. Output: Number of Black Fridays in the year as an integer. Examples: unluckyDays(2015) == 3 unluckyDays(1986) == 1 Note: In Ruby years will start from 1593.
"""

import datetime
def unlucky_days(year):
    return sum(1 for month in range(1, 13) if datetime.date(year, month, 13).weekday() == 4)

print(unlucky_days(1986))    # expect 1
print(unlucky_days(2015))    # expect 3
print(unlucky_days(2012))    # expect 3
print(unlucky_days(2022))    # expect 1
print(unlucky_days(2029))    # expect 2