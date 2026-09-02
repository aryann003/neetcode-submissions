from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def solve(n):
            if n == 0:
                return 1

            ans = 1
            for i in range(1, n + 1):
                ans = max(ans, i * solve(n - i))

            return ans

        ans = 0

        # Force the first split
        for i in range(1, n):
            ans = max(ans, i * solve(n - i))

        return ans