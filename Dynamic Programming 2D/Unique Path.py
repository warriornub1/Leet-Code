class Solution(object):
    def uniquePaths(self, m, n):
        res = []
        
        for _ in range(m):
            res.append([0] * n)
        
        # navigate through column
        for i in range(m):
            res[i][0] = 1
        
        # navigate through row
        for i in range(n):
            res[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i][j - 1] + res[i - 1][j]
        
        print(res[m - 1][n - 1])
        return res[m - 1][n - 1]
        
s = Solution()
s.uniquePaths(m = 3, n = 7)
        