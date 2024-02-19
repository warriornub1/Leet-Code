class Solution(object):
    def orangesRotting(self, grid):
    
        row, column = len(grid), len(grid[0])
        queue = []
        fresh, count = 0, 0
        visited = set()
        
        for x in range(row):
            for y in range(column):
                
                if grid[x][y] == 1:
                    fresh += 1
                
                elif grid[x][y] == 2:
                    queue.append((x, y))
        
        while queue and fresh:
            
            count += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                
                for addX, addY in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                    new_x, new_y = x + addX, y + addY
                    if(  -1 < new_x < row and -1 < new_y < column and grid[new_x][new_y] == 1 and 
                       (new_x, new_y) not in visited ):
                        
                        fresh -= 1
                        visited.add((new_x, new_y))
                        queue.append([new_x, new_y])
                        
        return count if fresh == 0 else -1            
         
s = Solution()
print(s.orangesRotting([[2,1,1],
                [1,1,0],
                [0,1,1]]))

print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

print(s.orangesRotting([[0,2]]))