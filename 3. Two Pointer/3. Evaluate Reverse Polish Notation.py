class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for operation in tokens:
            if operation == "+":
                stack.append( stack.pop() + stack.pop() )
            
            elif operation == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append( num1 - num2 )
            
            elif operation == "*":
                stack.append( stack.pop() * stack.pop() )
            
            elif operation == "/":
                stack.append( stack.pop() / stack.pop() )
            
            else:
                stack.append( int(operation) )
        
        return stack.pop()

s = Solution()
print( s.evalRPN( ["2","1","+","3","*"] ) )