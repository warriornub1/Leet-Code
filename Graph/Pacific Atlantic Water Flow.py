class Solution(object):
    def pacificAtlantic(self, heights):
        
        row, column = len(heights), len(heights[0])
        po, ao = set(), set()
        res = []
        
        def dfs(x, y, visited, prevHeight):
            
            if ( x < 0 or x >= row or y < 0 or y >= column or (x, y) in visited or
                heights[x][y] < prevHeight ):
                return
            
            visited.add( (x, y) )
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])
                
        
        for x in range(row):
            
            dfs(x, 0, po, heights[x][0])
            dfs(x, column - 1, ao, heights[x][column - 1])
        
        for y in range(column):
            
            dfs(0, y, po, heights[0][y])
            dfs(row - 1, y, ao, heights[row - 1][y])
        
        for x in range(row):
            for y in range(column):
                
                if (x, y) in po and (x, y) in ao:
                    res.append([x, y])
        
        print(res)
        return res
    
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

'''
heights = [[1,1],
           [1,1],
           [1,1]]
'''

s = Solution()
s.pacificAtlantic(heights)
