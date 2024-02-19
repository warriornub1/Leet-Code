# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 01:44:52 2024

@author: yongy
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        if not root:
            return 0
        return 1 + max(self.diameterOfBinaryTree(root.left),  self.diameterOfBinaryTree(root.right))

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(t))