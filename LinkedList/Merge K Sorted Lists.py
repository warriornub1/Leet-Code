# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:04:29 2024

@author: yongy
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
def mergeKLists(lists):
    
    if len(lists) == 0:
        return None
    
    while len(lists) > 1:
        merged_list = []
        for i in range(0, len(lists), 2):
            List1 = lists[i]
            List2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_list.append(mergeTwoList(List1, List2))
        lists = merged_list
        printAll(lists[0])

def mergeTwoList(List1, List2):
    
    dummyNode = ListNode(0)
    head = curr = dummyNode
    
    while List1 and List2:
        if List1.val < List2.val:
            curr.next = ListNode(List1.val)
            List1 = List1.next
        
        else:
            curr.next = ListNode(List2.val)
            List2 = List2.next
        curr = curr.next
        
    
    if List1:
        curr.next = List1
    elif List2:
        curr.next = List2
    
    #printAll(head.next)
    return head.next

def printAll(List):
    while List:
        print(List.val)
        List = List.next

list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
#mergeTwoList(list1, list2)

mergeKLists([list1, list2, list3])