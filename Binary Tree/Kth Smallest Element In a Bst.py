class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object): 
    
    def kthSmallest(self, root, k):
        
        if not root:
            return 0
        
        stack = []
        
        while True:
             
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
                
        '''
        res = []
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        print(res)
        return res[k - 1]
        '''

t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.left.right = TreeNode(2)

s = Solution()
print( s.kthSmallest(t1, 2) )
            