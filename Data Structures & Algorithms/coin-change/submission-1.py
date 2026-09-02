from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def solve(index,amount):
            if amount == 0:
                return 0
            if index >= len(coins):
                return float('inf')
            if coins[index] > amount:
                return float('inf')

            take = 1+solve(index,amount-coins[index])
            nottake = solve(index+1,amount)

            return min(take,nottake)
        result = solve(0,amount)
        if result == float('inf'):
            return -1
        return result