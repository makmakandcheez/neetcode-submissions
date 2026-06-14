class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming
        lowest = 999999
        maxP = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                maxP = max(maxP, price - lowest)
        
        return maxP
