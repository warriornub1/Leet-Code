class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        small_dist = float('inf')
        bestSum = None
        
        for index in range(len(nums) - 1):
            L, R = index + 1, len(nums) - 1
            while L < R:
                while nums[L - 1] == nums[L] and L < R:
                    L += 1
                
                total = nums[index] + nums[L] + nums[R]
                
                if total == target:
                    return total
                
                elif total < target:
                    L += 1
                else:
                    R -= 1
                
                dist = abs(total - target)
                if dist < small_dist:
                    small_dist = dist
                    bestSum = total
                    
                    
        return bestSum
        

s = Solution()
print(s.threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -14))