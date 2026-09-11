from functools import cache
import sys
sys.setrecursionlimit(20000)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @cache
        def solve(i):
            if i == len(s) - 1:
                return True

            for j in range(i + minJump, min(i + maxJump + 1, len(s))):
                if s[j] == '0' and solve(j):
                    return True

            return False

        return solve(0)