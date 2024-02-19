# Overall, the time complexity is O(n), and the space complexity is O(n) in the worst case

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root

        
        '''
        while True:
            if p.val <= root.val <= q.val:
                return root.val
            
            elif p.val <= root.val > q.val:
                root = root.left
            
            else:
                root= root.right

        '''


t = TreeNode(6)
t.left = TreeNode(2)
t.right = TreeNode(8)
t.right.left = TreeNode(7)
t.right.right = TreeNode(9)

t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.left = TreeNode(5)

p = TreeNode(2)
q = TreeNode(8)

s = Solution()
print(s.lowestCommonAncestor(t, p, q).val)


p = TreeNode(2)
q = TreeNode(4)
print(s.lowestCommonAncestor(t, p, q).val)