class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        
        def dfs(left, right, level):
            
            if not left and not right:
                return
            
            if level % 2 == 1:
                left.value, right.value = right.value, left.value
                
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)
        
        dfs(root.left, root.right, 1)
        return root
    
    def printAll(self, root):
        if not root:
            return
        
        print(root.value)
        self.printAll(root.left)
        self.printAll(root.right)
        
t1 = TreeNode(2)

t1.left = TreeNode(3)
t1.left.left = TreeNode(8)
t1.left.right = TreeNode(13)

t1.right = TreeNode(5)
t1.right.left = TreeNode(21)
t1.right.right = TreeNode(34)

s = Solution()
root = s.reverseOddLevels(t1)
s.printAll(root)
        