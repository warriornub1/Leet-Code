# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:25:36 2024

@author: yongy
"""

def exist(board, word):
    
    ROW, COLUMN = len(board), len(board[0])
    visited = set()
    
    def dfs(x, y, index):
        
        if index == len(word):
            return True
        
        if ( x < 0 or x >= ROW or y < 0 or y >= COLUMN or (x, y) in visited 
            or board[x][y] != word[index] ):
            return False
        
        visited.add((x, y))
        res =( dfs(x + 1, y, index + 1) or
        dfs(x - 1, y, index + 1) or
        dfs(x, y + 1, index + 1) or
        dfs(x, y - 1, index + 1) )
        visited.remove((x, y))
        return res
    
    for x in range(ROW):
        for y in range(COLUMN):
            if (x, y) not in visited and board[x][y] == word[0]:
                if dfs(x, y, 0):
                    return True
    return False

print(exist([["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]], 'ABCCED'))

print(exist([["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]], 'SEE'))

print(exist([["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]], 'ABCB'))