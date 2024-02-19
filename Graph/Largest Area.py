import collections
def maxAreaOfIsland(grid):
    
    visited = []
    row, column = len(grid), len(grid[0])
    largest_Area = 0
    
    def DFS(x, y):
        if (x not in range(row) 
        or y not in range(column) 
        or [x, y] in visited
        or grid[x][y] == 0):
            return 0
        
        visited.append([x, y])
        return 1 + DFS(x + 1, y) + DFS(x, y + 1) + DFS(x - 1, y) + DFS(x, y - 1)
    
    '''
    def BFS(x, y):
        
        queue = collections.deque()
        queue.append([x, y])
        visited.append([x, y])
        area = 1
        
        while queue:
            x, y = queue.popleft()
            for addX, addY in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_x, new_y = x + addX, y + addY
                if new_x in range(row) and new_y in range(column) and [new_x, new_y] not in visited \
                    and grid[new_x][new_y] == 1:
                    #print("{} {}".format(new_x, new_y))
                    area += 1
                    visited.append([new_x, new_y])
                    queue.append([new_x, new_y])
        print(area)
        return area
    '''
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1 and [i, j] not in visited:
                #print("X, Y : {} {}".format(i, j))
                largest_Area = max(largest_Area, DFS(i, j))
    
    print(largest_Area)
    return largest_Area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

maxAreaOfIsland(grid)