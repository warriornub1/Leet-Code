def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    pos = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            pos = i + 1
    
    return pos
print(canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
#print(canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))