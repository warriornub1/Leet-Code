# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:52:49 2024

@author: yongy
"""

class Solution(object):
    def threeSum(self, nums):
        
        nums = sorted(nums)
        Low, High = 1, len(nums) - 1
        res = []
        for index in range(len(nums) - 1):
            
            Low, High = index + 1, len(nums) - 1
            
            while Low < High:
                
                while nums[Low - 1] == nums[Low] and Low < High:
                    Low += 1
                
                total = nums[index] + nums[Low] + nums[High]
                print("{} {} {} {}".format(total, nums[index], nums[Low], nums[High]))
                if total == 0:
                    res.append([nums[index], nums[Low], nums[High]])
                    Low += 1
                    High -= 1
                    
                elif total < 0:
                    Low += 1
                    
                else:
                    High -= 1
        return res
    


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
