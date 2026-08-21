
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)+1)
        def solve(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i]+solve(i+2)
            nottake = solve(i+1)
            dp[i] = max(take,nottake)
            return dp[i]
            
        return solve(0)