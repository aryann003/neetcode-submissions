from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def solve(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            return solve(n-1)+solve(n-2)

        return solve(n)