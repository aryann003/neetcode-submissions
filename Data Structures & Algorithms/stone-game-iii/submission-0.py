from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue):

        n = len(stoneValue)

        @cache
        def solve(i):

            if i >= n:
                return 0

            ans = float('-inf')
            total = 0

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]

                ans = max(ans, total - solve(j + 1))

            return ans

        result = solve(0)

        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"