class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def rightSideView(self, root):
        
        res = []           
        queue = []
        if root:
            queue.append(root)
        
        while(queue):
            res.append(queue[0].val)
            for i in range(len(queue)):
                
                node = queue.pop(0)
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
        
        return res

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.right = TreeNode(5)
t1.right = TreeNode(3)
t1.right.right = TreeNode(4)

s = Solution()
print(s.rightSideView(t1))