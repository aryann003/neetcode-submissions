from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]):
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0

            right = solve(i,j+1)
            left = solve(i+1,j)

            return right + left
        if obstacleGrid[0][0] == 1:
            return 0
        return solve(0,0)
            
