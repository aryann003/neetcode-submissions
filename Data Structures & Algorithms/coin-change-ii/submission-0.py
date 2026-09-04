from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(index,amount):
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0

            take = solve(index,amount-coins[index])
            nottake = solve(index+1,amount)

            return take+nottake


        return solve(0,amount)