
# Time complexity : O(n^2)
# Space complexity : O(n) + O(log n)

def subsetsWithDup(nums):
    nums = sorted(nums)
    res = []
    
    def generateNum(index, ls):
        
        res.append(ls[::])
        
        #if ls not in res:
        #    res.append(ls[::])
        
            
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            ls.append(nums[i])
            generateNum(i + 1, ls)
            ls.pop()
            
    generateNum(0, [])
    return res
    
def merge(list1, list2):
    
    res = []
    l1, l2 = 0, 0
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            res.append(list1[l1])
            l1 += 1
        else:
            res.append(list2[l2])
            l2 += 1
    
    while l1 < len(list1):
        res.append(list1[l1])
        l1 += 1
        
    
    while l2 < len(list2):
        res.append(list2[l2])
        l2 += 1
    
    return res

def mergeSort(ls):
    
    if len(ls) == 1:
        return ls
    
    mid = len(ls) // 2
    left = mergeSort(ls[:mid])
    right = mergeSort(ls[mid:])
    
    return merge(left, right)
    
print(merge([2,4,6], [1,3,5]))

print(mergeSort([2, 3, 4, 6, 1, 2]))

print(subsetsWithDup([1,2,2]))
