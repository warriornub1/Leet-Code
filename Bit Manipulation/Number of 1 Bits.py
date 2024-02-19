class Solution(object):
    def hammingWeight(self, n):
        
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        
        print(res)
        
        
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        print(res)
        
        '''
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        
        
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        '''
    

s = Solution()
s.hammingWeight(1011)