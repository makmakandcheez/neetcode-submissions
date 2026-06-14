class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        maxP = 0
        i = 0
        for i in range(len(prices)-1):
            j = i + 1
            for j in range(j, len(prices)):
                if prices[j] - prices[i] > maxP:
                    maxP = prices[j] - prices[i]
        return maxP
