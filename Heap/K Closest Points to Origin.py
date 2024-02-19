import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        for point in points:
            x, y = point[0], point[1]
            dist = (x - 0)**2 + (y - 0)**2
            temp.append( (dist, x, y) )
            
        heapq.heapify(temp)
        for i in range(k):
            
            item = heapq.heappop(temp)
            res.append([item[1], item[2]])    
        
        return res

points = [[3,3],[5,-1],[-2,4]]
k = 2

s = Solution()
s.kClosest(points, k)