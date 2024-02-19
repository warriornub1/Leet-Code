class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def rangeSumBST(self, root, low, high):
        
        self.total = 0
        def dfs(node):
            
            if not node:
                return None
            
            if low <= node.val <= high:
                self.total += node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.total
    


t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(t, 7, 15))
