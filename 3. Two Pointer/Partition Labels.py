# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:17:47 2024

@author: yongy
"""

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        HashMap = dict()
        res = []
        for index, char in enumerate(s):
            HashMap[char] = index
        
        #print(HashMap)
        
        total = 0
        largest = HashMap[s[0]]
        for index, char in enumerate(s):
            total += 1
            largest = max(largest, HashMap[char])

            if index == largest:
                res.append(total)
                total = 0
                
        
        return res
        
s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))
print(s.partitionLabels('eccbbbbdec'))
print(s.partitionLabels('eaaaabaaec'))