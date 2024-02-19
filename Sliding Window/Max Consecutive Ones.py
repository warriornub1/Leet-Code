# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:22:19 2024

@author: yongy
"""

def findMaxConsecutiveOnes(nums):
    
    counter = 0
    longest = 0
    
    for index, num in enumerate(nums):
        if num == 0:
            counter = 0
        else:
            counter += 1
        
        longest = max(longest, counter)
    
    return longest

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))