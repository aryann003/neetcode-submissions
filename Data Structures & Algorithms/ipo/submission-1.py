import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap1 = []  # Min heap: (capital, profit)
        heap2 = []  # Max heap: (-profit, capital)

        # Store all projects in heap1
        for c, p in zip(capital, profits):
            heapq.heappush(heap1, (c, p))

        # Choose at most k projects
        for _ in range(k):

            # Move all affordable projects to the max heap
            while heap1 and heap1[0][0] <= w:
                c, p = heapq.heappop(heap1)
                heapq.heappush(heap2, (-p, c))

            # No affordable projects left
            if not heap2:
                break

            # Pick the project with the maximum profit
            p, c = heapq.heappop(heap2)
            w += -p

        return w