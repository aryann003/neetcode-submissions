class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] *(len(s))
        def solve(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]

            one = solve(i+1)

            two = 0

            if i+1 < len(s):
                num = int(s[i:i+2])
                if 10 <= num and num <= 26:
                    two = solve(i+2)

            dp[i] = one+two
            return dp[i]

        return solve(0)