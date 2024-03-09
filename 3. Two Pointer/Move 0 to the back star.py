# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:39:41 2024

@author: yongy
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return nums
        else:
            
            l, r = 0, 1
            while r < len(nums):
                
                if nums[l] != 0:
                    r += 1
                    l += 1
                    
                elif nums[r] == 0:
                    r += 1

                else:
                    temp = nums[r]
                    nums[r] = nums[l]
                    nums[l] = temp
                    
            return nums
                
                
                
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))

print(s.moveZeroes([2,1]))

#print(s.moveZeroes([1,0,1]))