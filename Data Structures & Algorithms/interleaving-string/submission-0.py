from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def solve(i,j,k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            
            if i < len(s1) and s1[i] == s3[k]:
                if solve(i+1,j,k+1):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if solve(i,j+1,k+1):
                    return True

            return False

        return solve(0,0,0)