class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        min_hour = float('inf')
        while start <= end:
            total_hour = 0
            mid = (start + end)//2

            for pile in piles:
                total_hour += math.ceil(pile/mid)

            if total_hour <= h:
                min_hour = mid
                end = mid-1
            else:
                start = mid+1

        return min_hour

