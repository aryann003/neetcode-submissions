import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x = sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            heapq.heappush(heap,(x,i))
        lst = []
        for i in range(k):
            dist,index = heapq.heappop(heap)
            lst.append(points[index])

        return lst
