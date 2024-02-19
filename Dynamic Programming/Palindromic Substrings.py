class Solution(object):
    
    def BruteForce(self, s):
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                res += self.IsPalindromeMovingInwards(s, i, j) 
    
        return res
    
    def IsPalindromeMovingInwards(self, s, l, r):
        
        while l < r:
            if s[l] != s[r]:
                return 0
            
            l += 1
            r -= 1
        return 1
    
    def countSubstrings(self, s):
        res = 0
        for index in range(len(s)):
            
            res += self.IsPalindrome( index, index, s )
            res += self.IsPalindrome( index, index + 1, s )
        
        return res
    
    
    def IsPalindrome(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) :
            if s[l] != s[r]:
                return res
            
            else:
                l -= 1
                r += 1
                
            res += 1
        return res
s = Solution()
print(s.countSubstrings("a"))
print(s.BruteForce("abc"))