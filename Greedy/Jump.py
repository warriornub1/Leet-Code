# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:22:41 2024

@author: yongy
"""

def jump(nums):

    G = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        print("{} {}".format(i + nums[i], nums[G]))
        if i + nums[i] >= G:
            G = i
    
    print(G)
    return G == 0
        
print(jump([1,1,2,5,2,1,0,0,1,3]))