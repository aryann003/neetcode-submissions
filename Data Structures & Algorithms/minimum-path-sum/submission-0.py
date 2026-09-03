from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]

            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')

            right = grid[i][j] + solve(i,j+1)
            down = grid[i][j] + solve(i+1,j)

            return min(right, down)
        
        return solve(0,0)