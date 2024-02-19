# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:57:55 2024

@author: yongy
"""

class Solution(object):
    def toCharArray(self, words):
        L, R = 0, 0
        total_max = 0
        total = 0
        bag = set()
        
        while R < len(words):
            
            bag.add(words[R])
            if len(bag) <= 2:
                total_max = max(total_max, R - L + 1)
                R += 1
            else:
                bag.remove(words[L])
                char = words[L]
                while words[L] == char:
                    L += 1
        
        return total_max

s = Solution()
print(s.toCharArray("eceba"))
#print(s.toCharArray("ccaabbb"))
#print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))