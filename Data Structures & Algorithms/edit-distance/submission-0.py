from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(i,j):
            if i >= len(word1):
                return len(word2)-j
            if j>= len(word2):
                return len(word1)-i
            if word1[i] == word2[j]:
                return solve(i+1,j+1)
            else:
                return 1+min({solve(i,j+1), solve(i+1,j), solve(i+1,j+1)
                })

        return solve(0,0)





            
