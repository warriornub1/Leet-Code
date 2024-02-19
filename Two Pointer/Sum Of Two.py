# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:39:41 2024

@author: yongy
"""

class Solution(object):
    def twoSum(self, numbers, target):
        
        l , r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            
            if total == target:
                return[l + 1, r + 1]
            
            elif total > target:
                r -= 1
            else:
                l += 1
                
        return[-1, -1]

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

print(s.twoSum([2, 3, 4], 6))

print(s.twoSum([-1], 0))