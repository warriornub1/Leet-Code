def subsets(candidates, target ):
    
    candidates = sorted(candidates)
    res = []
    
    def backtrack(index, total, ls):
        
        if total == target:
            res.append(ls[::])
            return
        
        if total > target or index >= len(candidates):
            return
        
        ls.append(candidates[index])
        backtrack(index + 1, total + candidates[index], ls)
        ls.pop()
        
        while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
            index += 1
        
        backtrack(index + 1, total, ls)

    
    backtrack(0, 0, [])
    return res
    

print(subsets([2,5,2,1,2] , 5))
#subsets([10,1,2,7,6,1,5] , 8)