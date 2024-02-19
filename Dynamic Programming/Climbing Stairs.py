class Solution(object):
    
    '''
    backtrack solution
    '''
    def recursive(self, n):
        
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        return self.recursive(n - 1) + self.recursive(n - 2)
   
    def recursive_top_down(self, n):
        
        '''
        originally time-complexity O(2^n)
        adding dp, changes the time-comeplxity to O(n)
        '''
        
        self.memory = [None] * (n + 1)
        def backtrack(n):
            
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            if self.memory[n] != None:
                return self.memory[n]
            
            self.memory[n] = backtrack(n - 1) + backtrack(n - 2)
            return self.memory[n]
        
        return backtrack(n) 
    
    def climbStairs(self, n):
        '''
        Time complexity: O(n)
        Space Complexity: O(n)
        '''

        if n <= 2:
            return n
        memory = [0, 1, 2]
        
        for i in range(3, n + 1):
            memory.append(memory[i - 1] + memory[i - 2])
        
        return memory[n]
        
    def BestSolution(self, n):
        '''
        Time complexity: O(n)
        Space Complexity: O(1)
        '''
        
        if n <= 2:
            return n
        
        prev = 1
        curr = 2
        for _ in range(3, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

s = Solution()
print(s.recursive(10))
print(s.recursive_top_down(10))
print(s.climbStairs(10))
print(s.BestSolution(10))