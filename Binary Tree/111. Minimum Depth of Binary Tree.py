class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def minDepth(self, root):
        
        self.depth = float('inf')
        
        def dfs(node, level):
            
            if not node:
                return
            
            if not node.left and not node.right:
                self.depth = min(self.depth, level + 1)
                return
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return self.depth
        
        '''
        if not root:
            return 0
        
        queue = []
        
        depth = 1
        queue.append(root)
        while(queue):
            
            for i in range(len(queue)):
                node = queue.pop(0)
                
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            depth += 1
        '''
        

t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)


s = Solution()
print(s.minDepth(t1))