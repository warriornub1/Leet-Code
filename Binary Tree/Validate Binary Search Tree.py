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
    def isValidBST(self, root):
        
        def dfs(node, smallest, largest):
            
            if not node:
                return True
            
            if smallest < node.val < largest:
                return dfs(node.left, smallest, node.val) and dfs(node.right, node.val, largest)
            
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))

t1 = TreeNode(5)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.right.left = TreeNode(3)


s = Solution()
print(s.isValidBST(t1))