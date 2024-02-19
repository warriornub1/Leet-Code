# the time complexity is O(2^n), where n is the length of the input list nums.

# Space Complexity: O(n) for the call stack + O(2^n) for the result

def subsets_For_Loop(nums):
    
    res = [[]]
    for n in nums:
        for r in range(len(res)):
            copy = res[r].copy()
            copy.append(n)
            res.append(copy)
    return res

    '''
    ans = [[]]
    for num in nums:
        for i in range(len(ans)):
            currSet = ans[i][::]
            currSet.append(num)
            ans.append(currSet)
            
    return ans
    '''

def subsets_For_Loop_Recursion(nums):
    
    res = []
    
    def recursion(ls, index):
        res.append(ls[::])
        
        for i in range(index, len(nums)):
            ls.append(nums[i])
            recursion(ls, i + 1)
            ls.pop()
    
    recursion([], 0)
    return res

def subsets(nums):
    
    res = []
    
    def backtrack(ls, index):
        
        if index >= len(nums):
            res.append(ls[::])
            return
        
        ls.append(nums[index])
        backtrack(ls, index + 1)
        ls.pop()
        backtrack(ls, index + 1)

    backtrack([], 0)
    return res
#print(subsets_For_Loop([1, 2, 3]))

#print(subsets_For_Loop_Recursion([1, 2, 3]))

print(subsets([1,2,3]))