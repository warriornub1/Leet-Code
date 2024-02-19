# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:12:12 2024

@author: yongy
"""

import heapq

# https://www.youtube.com/watch?v=58cYFs_W2_s&ab_channel=Amulya%27sAcademy

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print(heap)


# heappop will return the smallest value and also it will delete that 
# from the heap, maintaining the heap property
heapq.heappop(heap)
print(heap)

# heapify
list1 = [1, 3, 5, 2, 4, 6]
heapq.heapify(list1)
print("@@@@@@@@@@@@@@@@@")
print(list1)

list1 =  [1, 3, 5, 2, 4, 6]
heapq.heappushpop(list1, 1)
print(list1)

list1 = [(2, 'asd'), (1, 'asd')]
heapq.heapify(list1)
print(list1)

