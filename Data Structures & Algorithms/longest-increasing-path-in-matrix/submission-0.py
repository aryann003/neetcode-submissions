from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def solve(i,j,prev):
            if i<0 or j<0 or i>= len(matrix) or j>=len(matrix[0]):
                return 0

            if matrix[i][j] <= prev:
                return 0
            prev = matrix[i][j]
            return  1 + max({solve(i+1,j,prev), solve(i,j+1,prev), solve(i-1,j,prev), solve(i,j-1,prev)})

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, solve(i,j,float('-inf')))

        return ans

         