# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:30:08 2024

@author: yongy
"""

class Solution(object):
    def maxProfit(self, prices):
        
        bestPrice = float('inf')
        profit = 0
        for i, currPrice in enumerate(prices):
            if bestPrice > currPrice:
                bestPrice = currPrice
            
            else:
                profit = max(profit, currPrice - bestPrice)
        
        print(profit)
        return profit
        
    def bruteForce(self, prices):
        
        '''
        Time complexity: O(n^2)
        '''
        bestPrice = 0
        for i, currPrice in enumerate(prices):
            for j in range(i + 1, len(prices) ):
                bestPrice = max(bestPrice, prices[j] - currPrice )
                
        print(bestPrice)
        return bestPrice
    
s = Solution()
s.bruteForce([7, 1, 5, 3, 6, 4])
s.maxProfit([7, 1, 5, 3, 6, 4])