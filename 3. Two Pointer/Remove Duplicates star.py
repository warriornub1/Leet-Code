# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:20:14 2024

@author: yongy
"""

class Solution(object):
    def removeDuplicates(self, nums):
        
        
        if len(nums) < 2:
            return len(nums)
        
        l, r = 0 , 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
    
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([]))
print(s.removeDuplicates([1,2,3]))