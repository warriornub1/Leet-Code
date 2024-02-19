def robll(nums):
    if len(nums) == 1:
        return nums[0]
    loot = []
    loot.append(nums[0])
    loot.append(max([nums[0], nums[1]]))
    
    for i in range(2, len(nums)):
        
        number = max(loot[i - 2] + nums[i], loot[i - 1])
        loot.append( number )
    
    return loot[len(nums) - 1]

def rob(nums):
    skipLastHouse = []
    skipFirstHouse = []
    
    for i in range(len(nums) - 1):
        skipFirstHouse.append(nums[i])
        skipLastHouse.append(nums[i + 1])
    
    
    LootSkipFirstHouse = robll(skipFirstHouse)
    LootSkipLastHouse = robll(skipLastHouse)
    
    return(max(LootSkipFirstHouse, LootSkipLastHouse))
    
print(robll([2,3,2]))
#print(robll([1,2,3,1]))