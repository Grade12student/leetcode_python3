class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        buy = -prices[0]  # maximum profit if the first action is buying
        sell = 0  # maximum profit if the first action is selling
        for i in range(1, n):
            prev_buy = buy
            buy = max(buy, sell - prices[i])
            sell = max(sell, prev_buy + prices[i] - fee)
        return sell
