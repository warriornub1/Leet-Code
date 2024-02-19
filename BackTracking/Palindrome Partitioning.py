class Solution(object):
    def partition(self, s):
        
        res = []
        
        def backtrack(ls, index):
            
            if index == len(s):
                res.append(ls[::])
                
            for i in range(index, len(s)):
                
                if isPalindrome(s[index : i + 1]):
                    ls.append(s[index : i + 1])
                    backtrack(ls, i + 1)
                    ls.pop()
        
        def isPalindrome(word):
            i, j = 0, len(word) - 1
            
            while i < j:
                if word[i] != word[j]:
                    return False
                i, j = 1 + i, j - 1
            return True
        
        backtrack([], 0)
        return res
    
    
s = Solution()
print(s.partition("aab"))