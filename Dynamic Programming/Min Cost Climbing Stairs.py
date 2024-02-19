# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:16:34 2024

@author: yongy
"""

def minCostClimbingStairs(cost):
    cost_stairs = [0, 0]
    
    for index in range(2, len(cost) + 1):
        min_cost = min(cost_stairs[index - 1] + cost[index - 1], 
                       cost_stairs[index - 2] + cost[index - 2])
        cost_stairs.append(min_cost)
    
    return cost_stairs[len(cost)]

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
