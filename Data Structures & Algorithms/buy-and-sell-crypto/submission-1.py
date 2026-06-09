class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maximum = 0

        for price in prices:
            if price > buy:
                maximum = max(maximum, price - buy)
            if price < buy:
                buy = price
        return maximum
