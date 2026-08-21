class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp1 = [-1] *(len(nums)+1)
        dp2 = [-1] *(len(nums)+1)
        def solve(start,end,dp):
            if start >= end:
                return 0

            if dp[start] != -1:
                return dp[start]

            take = nums[start] + solve(start+2,end,dp)
            nottake = solve(start+1,end,dp)

            dp[start] = max(take,nottake)
            return dp[start]

        return max(solve(0,len(nums)-1,dp1),solve(1,len(nums),dp2))

        

        