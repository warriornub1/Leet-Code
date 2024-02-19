'''
Time complexity : O(m * n)
O(m * n) due to the space used by the visited set and the call stack during the recursive DFS calls

'''

class SolutionBFS:
    
    def numIslands(self, grid):
        row, column = len(grid), len(grid[0])
        
        visited = set()
        count = 0
        
        def dfs(x, y):
            if( x >= 0 and x < row and
            y >= 0 and y < column and
            (x, y) not in visited and
            grid[x][y] == "1" ):
                
                visited.add((x, y))
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
                    
        return count
        
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = SolutionBFS()
print(s.numIslands(grid))