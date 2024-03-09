class Solution(object):
    def maxArea(self, height):
        Low, High = 0, len(height) - 1
        
        if len(height) < 2:
            return 0
        
        maxArea = 0
        while Low < High:
            if height[Low] < height[High]:
                lowerHeight  = height[Low]
                area = lowerHeight * (High - Low)
                Low += 1
            else:
                lowerHeight  = height[High]
                area = lowerHeight * (High - Low)
                High -= 1
            
            maxArea = max(maxArea, area)
        return maxArea
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
#(s.maxArea([]))
#print(s.maxArea([1,2,3]))