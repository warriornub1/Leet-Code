class Solution:
    def twoSum(self, numbers, target ):
        l, r = 0, len(numbers) - 1
        while( l < r ):
            total = numbers[l] +  numbers[r]
            if total < target:
                l += 1
            
            if total > target:
                r -= 1
                
            else:
                return [ l + 1, r + 1 ]
                


s = Solution()
s.twoSum([2, 7, 11, 15], 9)