def twoSum(nums, target):
    hashmap = {}
    
    for index, num in enumerate( nums ):
        if target - num in hashmap:
            return [ hashmap[target - num], index ]
        else:
            hashmap[num] = index

print( twoSum( [2,7,11,15], 9 ) )
print( twoSum( [3,2,4], 6 ) )
print( twoSum( [3,3], 6 ) )