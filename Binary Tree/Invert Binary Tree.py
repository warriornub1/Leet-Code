class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def invertTree(self, root):
        
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        
t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.left = TreeNode(6)
t.right.right = TreeNode(9)

s = Solution()
node = s.invertTree(t)