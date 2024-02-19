# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:37:14 2024

@author: yongy
"""

class Solution(object):
    def LongeSubString(self, words):
        L = 0
        bag = set()
        longest = 0
        
        for R in range(len(words)):
            
            while words[R] in bag:
                bag.remove(words[L])
                L += 1
            bag.add(words[R])
            longest = max(longest, R - L + 1)
        return longest
        
s = Solution()
#print(s.LongeSubString ("abcad"))
print(s.LongeSubString ("abcb"))
#print(s.LongeSubString (""))
print(s.LongeSubString ("aaaa"))
print(s.LongeSubString ("pwwkew"))