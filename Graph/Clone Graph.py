'''
https://www.youtube.com/watch?v=vXkT2nYSde0
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        cloneMap = {}
        cloneMap[node] = Node(node.val)
        
        queue = [node]
        
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in cloneMap:
                    queue.append(neighbor)
                    cloneMap[neighbor] = Node(neighbor.val)
                    
                cloneMap[curr].neighbors.append(cloneMap[neighbor])
        
        return cloneMap[node]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1]
node3.neighbors = [node1]

graph1 = node1

s = Solution()
s.cloneGraph(graph1)