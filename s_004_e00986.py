# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:32:11 2022

@author: cukel
"""



def int32_to_ip(int32):
    return ".".join(map(str, [int32 >> 24, int32 >> 16 & 255, int32 >> 8 & 255, int32 & 255]))

print(int32_to_ip(2149583361))      # expect 128.32.10.1
print(int32_to_ip(32))              # expect 0.0.0.32
print(int32_to_ip(0))               # expect 0.0.0.0
print(int32_to_ip(1146351657))      # expect '68.83.240.41'
print(int32_to_ip(386722335))       # expect '23.12.234.31'