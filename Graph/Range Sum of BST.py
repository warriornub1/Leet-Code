class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    
    def rangeSumBST(self, root, low, high):
        
        def dfs(node):
            
            if not node:
                return 0
            
            current = 0
            if low <= node.val and node.val <= high:
                current = node.val
            
            return current + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    
t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(7)

t1.right = TreeNode(15)
t1.right.right = TreeNode(18)


s = Solution()
print(s.rangeSumBST(t1, 7, 15))