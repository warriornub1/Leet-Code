def brute_force(nums):
    
    '''
    Top down approach
    
    Time Complexity : 2^n
    Space Complexity : 2^n
    
    with memorization
    Time Complexity : n
    Space Complexity : n
    '''
    dp = [None] * len(nums)
    def backtracking(index):
        
        if dp[index] != None:
            return dp[index]
        
        if index == 0:
            return nums[index]
        
        if index < 0:
            return 0
        
        if index == 1:
            return max( nums[0], nums[1] )
        
        currHouse = backtracking(index - 2) + nums[index]
        prevHouse = backtracking(index - 1)
        dp[index] = max(currHouse, prevHouse)
        return dp[index]
    
    return backtracking( len(nums) - 1 )

def rob(nums):
    
    '''
    Bottom up approach
    using result array
    Time Complexity O(n)
    Space Complexity O(n)
    '''
    
    res = []
    res.append(nums[0])
    
    if len(nums) == 1:
        return res
    
    res.append(max( res[0], nums[1] ))
    for i in range(2, len(nums)):
        res.append( max( nums[i] + res[i - 2], res[i - 1] ) )

    
    return res[len(nums) - 1]

def Best(nums):
    
    '''
    Bottom up approach
    Time Complexity O(n)
    Space Complexity O(1)
    '''
    
    if len(nums) == 1:
        return nums[0]
    
    house1 = nums[0]
    house2 = max( house1, nums[1] )
    
    for i in range( 2, len(nums) ):
        tmp = house2
        house2 = max( house1 + nums[i], house2 )
        house1 = tmp

    
    return house2

#print(rob([1,2,3,1]))
print(brute_force([2,7,9,3,1]))
print(rob([2,7,9,3,1]))
print(Best([2,7,9,3,1]))