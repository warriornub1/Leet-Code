class Solution:
    def rotate(self, matrix):
        
        left, right = 0, len(matrix) - 1
        
        while( left < right ):
            
            for i in range(right - 1):
                top, bottom = left, right
                
                topLeft = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]
                
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                matrix[bottom][right - i] = matrix[top + 1][right]
                
                matrix[top + i][left] = topLeft
                
            left += 1
            right -= 1
            

s = Solution()
s.rotate( [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] )