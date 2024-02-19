class Solution(object):
    def generateParenthesis(self, n):
        
        res = []
        
        def generate(openN, closeN, ls):
            
            if openN == closeN == n:
                res.append("".join(ls))
                return
            
            if openN < n:
                ls.append("(")
                generate(openN + 1, closeN, ls)
                ls.pop()
                
            if closeN < openN:
                ls.append(")")
                generate(openN, closeN + 1, ls)
                ls.pop()
        
        generate(0, 0, [])
        return res
        
s = Solution()
print(s.generateParenthesis(3))