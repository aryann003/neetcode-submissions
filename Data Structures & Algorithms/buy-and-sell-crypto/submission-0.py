class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(len(prices)):
            buy = min(buy,prices[i])
            sell = max(buy, prices[i])
            profit = sell-buy
            max_profit = max(profit,max_profit)
        return max_profit