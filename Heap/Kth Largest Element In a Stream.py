# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:07:05 2024

@author: yongy
"""

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.size = k
        self.array = nums
        heapq.heapify(self.array)
        
        
        while len(self.array) > self.size:
            heapq.heappop(self.array)
        
        print(self.array)
        
    def add(self, item):
        heapq.heappush(self.array, item)
        while len(self.array) > self.size:
            heapq.heappop(self.array)
        
        return self.array[0]
        
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
#kthLargest.add(5)
#kthLargest.add(10)
#kthLargest.add(9)
#kthLargest.add(4)
