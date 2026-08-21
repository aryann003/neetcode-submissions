from functools import cache
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def solve(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            return solve(n-1)+solve(n-2)+solve(n-3)

        return solve(n)    