from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(s)
        heap = []
        for val,count in mp.items():
            heapq.heappush(heap,(-count,val))
        res = ""
        prev_char = ""
        prev_cnt = 0
        while heap:
            count , val = heapq.heappop(heap)
            res += val
            count += 1
            if prev_cnt != 0:
                heapq.heappush(heap,(prev_cnt,prev_char))
            prev_char = val
            prev_cnt = count
        if len(res) != len(s):
            return ""

        return res

