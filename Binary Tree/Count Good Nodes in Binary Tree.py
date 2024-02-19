class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def goodNodes(self, root):
        
        def dfs(node, largest):
            
            if not node:
                return 0
            
            res = 1 if node.val >= largest else 0
            largest = max(largest, node.val)
            return res + dfs(node.left, largest) + dfs(node.right, largest)
    
        return dfs(root, root.val)
    
t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.left.left = TreeNode(3)

t1.right = TreeNode(4)
t1.right.left = TreeNode(1)
t1.right.right = TreeNode(5)

s = Solution()
print(s.goodNodes(t1))