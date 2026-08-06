from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)

        heap = []
        for f in mp.values():
            heapq.heappush(heap,-f)
        ans = 0
        while heap:
            queue = []

            for i in range(n+1):
                if heap:
                    ans += 1
                    cnt = heapq.heappop(heap)
                    if cnt + 1 != 0:
                        queue.append(cnt + 1)

                else:
                    if queue:
                        ans += 1
            while queue:
                heapq.heappush(heap,queue.pop())

        return ans




