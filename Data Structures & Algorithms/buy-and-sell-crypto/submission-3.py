class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two Pointers
        l = 0
        r = 1
        maxP = 0
        while r < (len(prices)):
            if prices[r] > prices[l]:
                maxP = max(maxP, prices[r] - prices[l])
            elif prices[r] < prices[l]:
                l = r
            r += 1
        return maxP 

