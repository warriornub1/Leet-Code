# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
    

class Solution(object):
    
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        depth = 0
        if root.children:
            for c in root.children:
                depth = max(depth, self.maxDepth(c))
            
        return depth+1
    
    
    
    def DFS(self, root):
        
        self.depth = 0
        queue = []
        
        if root:
            queue.append(root)        
                
        while queue:
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                
                if node.children:
                    for c in node.children:
                        queue.append(c)
                    
            self.depth += 1

        return self.depth

root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
s = Solution()
print(s.maxDepth(root))