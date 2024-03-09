def topKFrequent(nums, k):
    hashmap = {}
    res = [0] * len(nums)

    
    for number in nums:
        hashmap[number] = 1 + hashmap.get( number, 0 )
    
    for key, total in hashmap.items():
        res[total] = key
    
    rtn = []
    for i in range(len(res) - 1, -1, -1):
        if res[i] != 0:
            rtn.append(res[i])
            k -= 1
        if k == 0:
            return rtn


print( topKFrequent( [1,1,1,2,2,3], 2 ) )