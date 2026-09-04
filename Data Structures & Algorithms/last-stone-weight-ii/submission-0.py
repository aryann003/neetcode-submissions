from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # summ = sum(stones)
        @cache
        def solve(index, summ):
            if index == len(stones):
                return abs(summ)

            pos = solve(index+1, summ+stones[index])
            neg = solve(index+1, summ-stones[index])

            return min(pos,neg)
        
        return solve(0,0)