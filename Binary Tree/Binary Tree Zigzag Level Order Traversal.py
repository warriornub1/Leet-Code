# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:58:00 2024

@author: yongy
"""

import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    
    if not root:
        return []
    
    res = []
    queue = collections.deque()
    queue.append(root)
    going_right = True
    
    while queue:
        
        tmp = []
        for _ in range(len(queue)):
            
            if going_right:
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            else:
                node = queue.pop()
                tmp.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                    
                if node.left:
                    queue.appendleft(node.left)
                    
        going_right = not going_right
        res.append(tmp)
        
    print(res)
    return res
    '''
    if not root:
        return []
    res = []
    queue = collections.deque([root])
    going_right = True
    
    while queue:
        level_items = []
        
        for _ in range(len(queue)):
            if going_right:
                top = queue.popleft()
                
                level_items.append(top.val)
            
                if top.left:
                    queue.append(top.left)
                    
                if top.right:
                    queue.append(top.right)
            
            else:
                top = queue.pop()
                
                level_items.append(top.val)
                
                if top.right:
                    queue.appendleft(top.right)
                
                if top.left:
                    queue.appendleft(top.left)
                    
        res.append(level_items)
        
        going_right = not going_right
    
    print(res)
    return res
    '''
n1 = Node(3)
n1.left = Node(9)
n1.right = Node(20)

n1.left.left = Node(1)
n1.left.right = Node(10)

n1.right.left = Node(15)
n1.right.right = Node(7)

zigzagLevelOrder(n1)
