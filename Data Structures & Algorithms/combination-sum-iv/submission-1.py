from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(target):
            if target == 0:
                return 1

            if target < 0:
                return 0
            ans = 0
            for num in nums:
                ans += solve(target-num)

            return ans

        return solve(target)
            
