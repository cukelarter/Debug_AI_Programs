# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:41:48 2022

@author: Luke

The Vigenère cipher is a classic cipher that was thought to be "unbreakable" for three centuries. We now know that this is not so and it can actually be broken pretty easily. How the Vigenère cipher works: The basic concept is that you have a message and a key, and each character in the message is encrypted using a character in the key, by applying a Caesar shift. The key is recycled as many times as needed. You might want to try this kata first, which focuses on the encryption and decryption processes. Well how do we break it? The first thing we have to do is determine the length of the key that was used to encrypt the message. Write a function that takes some cipher text and a maximum possible key length and returns the length of the key that was used in the encryption process. Note: We don't care about what characters are in the key -- only how many of them there are. Any feedback (and suggestions) would be much appreciated This kata is based on one of the programming assignments in Prof. Jonathan Katz's course on cryptography given on Coursera

this is a big fish
"""

def get_key_length(cipher_text, max_key_length):
    # get the length of the cipher text
    length = len(cipher_text)
    # create a list to store the key length
    key_length = []
    # loop through the possible key length
    for i in range(1,max_key_length+1):
        # create a list to store the number of matches
        matches = []
        # loop through the cipher text
        for j in range(i,length,i):
            # check if the cipher text is the same as the cipher text shifted by i
            if cipher_text[j] == cipher_text[j-i]:
                # append the number of matches
                matches.append(1)
        # append the key length
        key_length.append(sum(matches))
    # return the key length
    return key_length.index(max(key_length))+1

print(get_key_length("abc",3))
print(get_key_length("cba",3))

#%%

from string import ascii_uppercase as l

class CypherTable:
   def __init__(self):
      self.final_table = [l[i:]+l[:i] for i in range(len(l))]

for i in CypherTable().final_table:
    print(i)
    
