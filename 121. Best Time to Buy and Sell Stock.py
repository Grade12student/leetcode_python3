class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]  # Initialize min_price to the first element
        max_profit = 0
        for i in prices[1:]:
            if i < min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit
