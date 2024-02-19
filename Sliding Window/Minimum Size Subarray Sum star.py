# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:57:55 2024

@author: yongy
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        L, R = 0, 0
        total = 0
        length = float('inf')
        
        while R < len(nums):
            total += nums[R]
            
            while total >= target and L <= R:
                print("{} {}".format(R, L))
                length = min(length, R - L + 1)
                #print(length)
                total -= nums[L]
                L += 1
                
            R += 1
                
        return length

s = Solution()
#print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(4, [1,4,4]))
#print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))