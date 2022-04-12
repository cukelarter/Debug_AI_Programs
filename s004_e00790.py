# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:29:23 2022

@author: Luke

Your task is to write two functions:

to_utf8_binary: which encodes a string to a bitstring using UTF-8 encoding.
from_utf8_binary: which does the reverse.
Layout of UTF-8 byte sequences:
# BYTES  FIRST CODE POINT  LAST CODE POINT    BYTE 1      BYTE 2      BYTE 3      BYTE 4
  1                   0              127    0xxxxxxx  
  2                 128             2047    110xxxxx    10xxxxxx
  3                2048            65535    1110xxxx    10xxxxxx    10xxxxxx  
  4               65536          1114111    11110xxx    10xxxxxx    10xxxxxx    10xxxxxx
"""


def to_utf8_binary(string):
    return ''.join(['{:08b}'.format(ord(i)) for i in string])

def from_utf8_binary(string):
    return ''.join([chr(int(string[i:i+8], 2)) for i in range(0, len(string), 8)])

print(to_utf8_binary('1000001'))
print(to_utf8_binary('101000101101011'))


#%%
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result