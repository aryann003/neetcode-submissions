class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0
        for p in prices:
            buy = min(sell,p)
            sell = max(buy,p)
            profit += sell-buy
        return profit