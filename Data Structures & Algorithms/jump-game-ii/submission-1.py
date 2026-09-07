class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i == len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]

            ans = float('inf')

            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    ans = min(ans, 1 + solve(i + j))

            memo[i] = ans
            return ans

        return solve(0)