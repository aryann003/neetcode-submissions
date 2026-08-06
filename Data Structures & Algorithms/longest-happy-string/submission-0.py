import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heapq.heappush(heap,(-a,'a'))
        if b:
            heapq.heappush(heap,(-b,'b'))
        if c:
            heapq.heappush(heap,(-c,'c'))

        res = ""

        while heap:

            cnt1, ch1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:

                if not heap:
                    break
                
                cnt2, ch2 = heapq.heappop(heap)

                res += ch2

                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(heap,(cnt2,ch2))
                heapq.heappush(heap,(cnt1,ch1))

            else:
                res += ch1
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(heap,(cnt1,ch1))

        return res
