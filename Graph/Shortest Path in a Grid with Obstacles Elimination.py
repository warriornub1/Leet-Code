class Solution(object):
    def shortestPath(self, grid, k):

        row, column = len(grid), len(grid[0])
        goalx, goaly = row - 1, column - 1
        queue = []
        visited = set()
        
        queue.append([0, 0, k, 0])
        
        while queue:
            
            x, y, hammer, step = queue.pop(0)
            
            if x == goalx and y == goaly:
                return step
            
            if(x, y, hammer) not in visited:
                visited.add((x, y, hammer))
                for add_x, add_y in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                    new_x, new_y = x + add_x, y + add_y
                    
                    if( new_x >= 0 and new_x < row and
                       new_y >= 0 and new_y < column):
                        
                        if grid[new_x][new_y] == 1 and hammer > 0:
                            queue.append([new_x, new_y, hammer - 1, step + 1])
                        
                        elif grid[new_x][new_y] == 0:
                            queue.append([new_x, new_y, hammer, step + 1])
                                            
        return -1
    
s = Solution()

grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]

print(s.shortestPath(grid, 1))

grid = [[0,1,1],
        [1,1,1],
        [1,0,0]]

print(s.shortestPath(grid, 1))

grid = [[0]]

print(s.shortestPath(grid, 1))
        