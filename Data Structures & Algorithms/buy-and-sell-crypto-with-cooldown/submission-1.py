from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def solve(index, profit, flag):

            if index >= len(prices):
                return profit

            if not flag:
                return max(
                    solve(index + 1, profit - prices[index], True),
                    solve(index + 1, profit, False)
                )

            else:
                return max(
                    solve(index + 2, profit + prices[index], False),
                    solve(index + 1, profit, True)
                )

        return solve(0, 0, False)