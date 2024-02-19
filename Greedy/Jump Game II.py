# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:22:41 2024

@author: yongy
"""

def jumpll(nums):
    
    L = R = 0
    count = 0
    while R < len(nums) - 1:
        
        nextJump = 0
        for i in range (L , R + 1):
            nextJump = max(nextJump, nums[i] + i)
        
        L = R + 1
        R = nextJump
        count += 1
    return count
print(jumpll([2,3,1,1,4]))