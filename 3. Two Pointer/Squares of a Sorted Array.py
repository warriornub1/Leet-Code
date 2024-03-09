# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:07:31 2024

@author: yongy
"""

# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        rtn = [None for _ in range(len(nums))]
        index = len(nums) - 1
        L, R = 0, index
        
        while L <= R:
            print("{} {}".format(L, R))
            numR, numL = nums[R] ** 2, nums[L] ** 2
            if numR > numL:
                rtn[index] = numR
                R -= 1
            else:
                rtn[index] = numL
                L +=1
            
            index -= 1
        return rtn
    
s = Solution()

print(s.sortedSquares([-4,-1,0,3]))

#print(s.sortedSquares([-10000,-9999,-7,-5,0,0,10000]))
