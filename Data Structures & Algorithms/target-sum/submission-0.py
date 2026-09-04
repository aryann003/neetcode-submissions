from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def solve(index,target):
            if index == len(nums):
                if target == 0:
                    return 1
                return 0

            add = solve(index+1,target + nums[index])
            sub = solve(index+1,target - nums[index])

            return add+sub

        return solve(0,target)
        