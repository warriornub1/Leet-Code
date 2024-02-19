# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:57:12 2024

@author: yongy
"""

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
   def isSameTree(self, root, subRoot):
       
       if not root and not subRoot:
           return True
       
       if root and subRoot and root.val == subRoot.val:
           return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
       
       else:
           return False
        
t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(5)
#t.left.left = TreeNode(1)
#t.left.right = TreeNode(2)

t1 = TreeNode(3)
t1.left = TreeNode(4)
t1.right = TreeNode(5)


s = Solution()
print(s.isSameTree(t, t1))