class Solution(object):
    def letterCombinations(self, digits):

        Keypad = { "2": "abc", 
            "3" : "def", 
            "4" : "ghi", 
            "5" : "jkl", 
            "6" : "mno", 
            "7" : "pqrs", 
            "8" : "tuv", 
            "9" : "wxyz"}
        
        res = []
        
        def backtrack(index, word):
            
            if index == len(digits):
                res.append(word)
                return
            
            for c in Keypad[digits[index]]:
                backtrack( index + 1, word + c )
                
        backtrack(0, "")
        return res
        
s = Solution()
print(s.letterCombinations("23"))