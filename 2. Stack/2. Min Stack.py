class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print( minStack.getMin() ) # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2