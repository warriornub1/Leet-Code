class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = []
        if root:
            queue.append(root)
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(tmp)
        return res


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.left.left = TreeNode(100)
t.left.right = TreeNode(200)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(t))