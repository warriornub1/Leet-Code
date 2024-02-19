class Solution(object):
    def solve(self, board ):
        
        row, column = len(board), len(board[0])
        visited = set()
        
        
        def dfs(x, y):
            
            if ( x < 0 or x >= row or y < 0 or y >= column or board[x][y] == "X" or (x, y) in visited ):
                return
            
            board[x][y] = "T"
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            
            
        for x in range(row):
            for y in range(column):
                if ( x in (0, row - 1) or y in (0, column - 1) ):
                    if board[x][y] == "O":
                        dfs(x, y)
        
        for x in range(row):
            for y in range(column):
                if board[x][y] == "O":
                    board[x][y] = "X"
        
        for x in range(row):
            for y in range(column):
                if board[x][y] == "T":
                    board[x][y] = "O"
        
        print(board)
        return board

s = Solution()
    
s.solve([["X","X","X","X"],
       ["X","O","O","X"],
       ["X","X","O","X"],
       ["X","O","X","X"]])

s.solve([["X"]])
