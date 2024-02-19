# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:09:56 2024

@author: yongy
"""

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def balanceTree(self, root):
        
        def dfs(node):
            
            if not node:
                return [0, True]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            isBalance = abs(left[0] - right[0]) <= 1 
            
            return [1 + max(left[0], right[0]), isBalance and left[1] and right[1]]
        
        return dfs(root)[1]
        
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)


t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.left = TreeNode(3)
t2.left.right = TreeNode(3)
t2.left.left.left = TreeNode(4)
t2.left.left.right = TreeNode(4)


s = Solution()
print(s.balanceTree(t1))