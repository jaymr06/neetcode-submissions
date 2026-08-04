class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] - min(prices[:sell]) > profit:
                profit = prices[sell] - min(prices[:sell])
        return profit