# In summary, the time complexity is O(n!) and the space complexity is O(n).

class Solution(object):
    def permute(self, nums):
        
        res = []
        
        def backtrack(ls, temp):
            
            if len(temp) == 0:
                res.append(ls[::])
                return
            
            for i in range(len(temp)):
                copy = temp.copy()
                number = copy.pop(i)
                ls.append(number)
                backtrack(ls, copy)
                ls.pop()
        
        backtrack([], nums)
        return res
                
    
s = Solution()
print(s.permute([1, 2, 3]))