# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:02:04 2024

@author: yongy
"""

class Solution(object):
    def partition(self, s):
        
        res = []
        def findWord(index, ls):
            if index >= len(s):
                res.append(ls[::])
                return
            
            for j in range(index, len(s)):
                if self.isPalindrome(s, index, j):
                    ls.append(s[index: j + 1])
                    findWord(j + 1, ls)
                    ls.pop()
        
        findWord(0, [])
        print(res)
        return res

    def isPalindrome(self, s, l, r):
        
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

s = Solution()
s.partition("aabb")