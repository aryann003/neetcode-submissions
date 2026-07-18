class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        min_weight = 0
        while l <= r:
            mid = (l+r) // 2
            total = 0
            ships = 1

            for i in range(len(weights)):
                total += weights[i]
                if total > mid:
                    ships += 1
                    total = weights[i]
            if ships > days:
                l = mid+1
            else:
                min_weight = mid
                r = mid-1
        return min_weight


