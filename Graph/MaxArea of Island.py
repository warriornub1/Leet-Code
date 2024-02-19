'''
Time complexity : O(m * n)
O(m * n) due to the space used by the visited set and the call stack during the recursive DFS calls

'''

class SolutionBFS:
    
    def maxAreaOfIsland(self, grid):
        row, column = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        
        def dfs(x, y):
            if ( x < 0 or x >= row or y < 0 or y >= column or
                grid[x][y] == 0 or (x, y) in visited ):
                    return 0
            else:
                visited.add( (x, y) )
                return (1 + 
                dfs(x + 1, y) +
                dfs(x - 1, y) + 
                dfs(x, y + 1) +
                dfs(x, y - 1) )
        
        for x in range( row ):
            for y in range( column ):
                if grid[x][y] == 1 and (x, y) not in visited:
                    maxArea = max(maxArea, dfs(x,y))
        
        return maxArea
        
        
grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]

s = SolutionBFS()
print(s.maxAreaOfIsland(grid))
