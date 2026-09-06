from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def solve(i,j):
            if j == len(p):
                return i == len(s)

            
            first = i < len(s) and (s[i] == p[j] or p[j] == '.')


            if j+1 < len(p) and p[j+1] == '*':

                return solve(i,j+2) or (first and solve(i+1,j))

            if first:
                return solve(i+1,j+1)
            return False

        return solve(0,0)