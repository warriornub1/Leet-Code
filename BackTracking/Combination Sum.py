# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:11:03 2024

@author: yongy
"""

# Time Complexity : O(2 ^ n)
# Space Complexity : O(n) + O(2 ^ n)

def combinationSum(candidates, target):
    
    res = []
    def backtrack(total, ls, index):
        
        if total == target:
            res.append(ls[::])
            return
        
        if total > target or index >= len(candidates):
            return
        
        ls.append(candidates[index])
        backtrack(total + candidates[index], ls, index)
        ls.pop()
        backtrack(total, ls, index + 1)
        
    
    backtrack(0, [], 0)
    return res

print(combinationSum([2,3,6,7], 7))
#print(combinationSum([10,1,2,7,6,1,5], 8))