# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:36:25 2022

@author: Luke

The borrowers are tiny tiny fictional people. As tiny tiny people they have to be sure they aren't spotted, or more importantly, stepped on. As a result, the borrowers talk very very quietly. They find that capitals and punctuation of any sort lead them to raise their voices and put them in danger. The young borrowers have begged their parents to stop using caps and punctuation. Change the input text 's' to new borrower speak. Help save the next generation!
"""

def borrow(s):
    import string
    return s.lower().translate(str.maketrans('','',string.punctuation))

print(borrow('Help me I am a NORMAL HUMAN trapp[ed in the body of a; BoRRoWer!!'))
print(borrow('Here is some Punctuation: >? + / $'))
print(borrow('The quick BROwN fox J.ump?s OvEr the Lazy Dog!'))
print(borrow('HELLO!!!! WORLD!!!!'))
print(borrow("I won't take < a 50% cut."))