class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        curr = 0

        for p, f, t in trips:
            while heap and heap[0][0] <= f:
                e, cap = heapq.heappop(heap)
                curr -= cap

            curr += p
            if curr > capacity:
                return False
            heapq.heappush(heap, (t,p))

        return True
