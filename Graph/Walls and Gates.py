# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:38:12 2024

@author: yongy
"""

class SolutionBFS:
    
    def numIslands(self, grid):
        
        queue = []
        visited = set()
        count = 0
        
        row, column = len(grid), len(grid[0])
        
        for x in range(row):
            for y in range(column):
                if grid[x][y] == 0:
                    queue.append([x, y])
                    visited.add((x, y))
                    
        while queue:
            
            count += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for addX, addY in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                    
                    newX, newY = x + addX, y + addY
                    if ( -1 < newX < row and -1 < newY < column and grid[newX][newY] == INF and (newX, newY) not in visited ):
                        visited.add((newX, newY))
                        grid[newX][newY] = count
                        queue.append( [newX, newY]) 
        
        print(grid)
        
INF = 2147483647
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]
s = SolutionBFS()
s.numIslands(rooms)