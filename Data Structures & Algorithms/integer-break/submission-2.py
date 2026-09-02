from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:

        @cache
        def solve(n, must_split):
            if n == 0:
                return 1

            ans = 0

            for i in range(1, n + 1):
                if i == n and must_split:
                    continue

                ans = max(ans, i * solve(n - i, False))

            return ans

        return solve(n, True)