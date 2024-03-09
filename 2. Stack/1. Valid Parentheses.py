class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ")" : "(", "}" : "{", "]" : "[" }
        stack = []
        
        for bracket in s:
            
            if bracket in hashmap:
                if len(stack) == 0 or stack[-1] != hashmap[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        return len(stack) == 0
    

s = Solution()
print( s.isValid("()[]{}") )
print( s.isValid("(]") )