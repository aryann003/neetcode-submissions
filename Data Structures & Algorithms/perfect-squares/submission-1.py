from functools import cache
import sys
sys.setrecursionlimit(20000)
class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def solve(n):
            if n == 0:
                return 0 
            if n < 0:
                return float('inf')
            ans = float('inf')
            for i in range(1,int(n**0.5)+1):
               ans = min(ans,1+solve(n-(i*i))) 
            return ans

        return solve(n)