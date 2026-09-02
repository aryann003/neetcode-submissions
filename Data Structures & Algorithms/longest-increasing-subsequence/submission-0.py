from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def solve(index, prev):
            if index == len(nums):
                return 0
            
            if nums[index] > prev:
                return max(1+solve(index+1, nums[index]), solve(index+1,prev))

            else:
                return solve(index+1,prev)

        return solve(0,float('-inf'))