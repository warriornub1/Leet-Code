# Time Complexity O(n * m * 4 ^n)

class Solution(object):
    def exist(self, board, word):
        
        row, column = len(board), len(board[0])
        visited = set()
        
        def dfs( x, y, index ):
            
            if index == len(word):
                return True
    
            if ( x < 0 or y < 0 or
                x >= row or y >= column or
                index == len(word) or (x, y) in visited or 
                board[x][y] != word[index] ):
                return False
            
            
            visited.add((x, y))
            
            res = ( dfs(x + 1, y, index + 1) or dfs(x - 1, y, index + 1) or 
                    dfs(x, y - 1, index + 1) or dfs(x, y + 1, index + 1) )
            
            visited.remove((x, y))
            return res
        
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
        return False
    
s = Solution()
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","F","E","E"]]
word = "ABCCED"
print( s.exist(board, word) )