class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]
        
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        
        return res
        
s = Solution()
print( s.singleNumber([4,1,2,1,2]) )