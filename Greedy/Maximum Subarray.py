# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 01:09:07 2024

@author: yongy
"""

def maxSubArray(nums):
    
    largest = nums[0]
    total = 0
    for i in range(len(nums)):

        total += nums[i]
        largest = max(total, largest)
        if total < 0:
            total = 0
    print(largest)
        

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])