class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def invertTree(self, root):
        
        if not root:
            return 0
        
        return 1 + max(self.invertTree(root.left), self.invertTree(root.right))



t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.invertTree(t))
