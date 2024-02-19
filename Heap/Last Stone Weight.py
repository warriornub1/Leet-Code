# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:41:22 2024

@author: yongy
"""

import heapq

class KthLargest(object):

    def lastStoneWeight(self, stones):
        arr = [-1 * num for num in stones]
        heapq.heapify(arr)
        while len(arr) != 1:
            firstNum = heapq.heappop(arr)
            secNum = heapq.heappop(arr)
            
            if firstNum != secNum:
                heapq.heappush(arr, -1 * abs(firstNum - secNum))
        return -1 * arr[0]
        
k = KthLargest()
print(k.lastStoneWeight([2,7,4,1,8,1]))