# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:07:53 2024

@author: yongy
"""

def longest(words, k):
    
    longest = 0
    L = 0
    bag = set()
    for R in range(len(words)):
        bag.add(words[R])
        while len(bag) > k:
            bag.remove(words[L])
            L += 1
            
        print(bag)
        
        longest = max(longest, R - L + 1)
        print(longest)

longest("eceba", 2)