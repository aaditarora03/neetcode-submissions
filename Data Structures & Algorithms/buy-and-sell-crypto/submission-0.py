class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(1, len(prices)):
            for j in range(i):
                if prices[i] - prices[j] > max:
                    max = prices[i] - prices[j]
        return max