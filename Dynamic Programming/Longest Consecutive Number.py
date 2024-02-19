class Solution(object):
    def longestConsecutive(self, nums):
        number_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in number_set:
                length = 0
                while num in number_set:
                    num += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
    
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))