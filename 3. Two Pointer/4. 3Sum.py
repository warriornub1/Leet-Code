class Solution:
    def threeSum(self, nums):
        nums = self.mergeSort(nums)
        
        res = []
        for i, value in enumerate(nums):
            
            if value == 0:
                break
            
            if i > 0 and value == nums[i - 1]:
                continue
            
            l, j = i + 1, len(nums) - 1
            
            while l < j:
                
                total = value + nums[l] + nums[j]
                
                if total == 0:
                    res.append( [ value, nums[l], nums[j] ] )
                    l += 1
                    j -= 1
                    while nums[l] == nums[l - 1] and l < j:
                        l += 1
                    
                elif total < 0:
                    l += 1
                
                else:
                    j -= 1
                    
        return res
        
    def merge(self, list1, list2):
        
        i, j = 0, 0
        res = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            
            else:
                res.append(list2[j])
                j += 1
        
        while i < len(list1):
            res.append(list1[i])
            i += 1
        
        while j < len(list2):
            res.append(list2[j])
            j += 1
        
        return res
        
    def mergeSort(self, list1):
        
        if len(list1) == 1:
            return list1
        
        mid = len(list1) // 2
        L = self.mergeSort(list1[:mid])
        R = self.mergeSort(list1[mid:])
            
        return self.merge(L, R)
            
            
S = Solution()
print( S.threeSum([-1,0,1,2,-1,-4]) )